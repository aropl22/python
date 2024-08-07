import boto3
import datetime
import re

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

from botocore.exceptions import ClientError


def lambda_handler(event, context):
    # Create a Cost Explorer client
    client = boto3.client('ce')

    # Set time range to cover the last full calendar month
    # Note that the end date is EXCLUSIVE (e.g., not counted)
    now = datetime.datetime.utcnow()
    print ('Report created: '+str(now)+' (UTC)')
    # Set the end of the range to start of the current month
    #end = datetime.datetime(year=now.year, month=now.month, day=1)
    reportday = datetime.datetime(year=now.year, month=now.month, day=now.day)

    # Subtract a day and then "truncate" to the start of previous month
    #start = end - datetime.timedelta(days=1)
    start = reportday - datetime.timedelta(days=1)
    start = datetime.datetime(year=start.year, month=start.month, day=start.day)
    # Get the month as string for email purposes
    reporttime = start.strftime('%Y-%m-%d')



    # Convert them to strings
    start = start.strftime('%Y-%m-%d')
    #end = end.strftime('%Y-%m-%d')
    reportday = reportday.strftime('%Y-%m-%d')
    print('Report for: '+start)
    #print(end)
    #print('Raport Day: '+reportday)

    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': start,
            'End':  reportday
        },
        #Granularity='MONTHLY',
        Granularity='DAILY',
        Metrics=['BlendedCost'],
        GroupBy=[
            {
                'Type': 'TAG',
                'Key': 'Client'
            },
        ]
    )

    response1 = client.get_cost_and_usage(
        TimePeriod={
            'Start': start,
            'End':  reportday
        },
        #Granularity='MONTHLY',
        Granularity='DAILY',
        Metrics=['BlendedCost'],
        GroupBy=[
            {
                'Type': 'TAG',
                'Key': 'Service'
            },
        ]
    )

    response2 = client.get_cost_and_usage(
        TimePeriod={
            'Start': start,
            'End':  reportday
        },
        #Granularity='MONTHLY',
        Granularity='DAILY',
        Metrics=['BlendedCost'],
        GroupBy=[
            {
                'Type': 'TAG',
                'Key': 'Stack'
            },
        ]
    )
    
    #Get "By Client Report"

    tsv_lines = ['By Client: \n']
    total_cost=0
    print ('\nBy Client: \n')
    for project in response["ResultsByTime"][0]["Groups"]:
        namestring = project['Keys'][0]
        name = re.search("\$(.*)", namestring).group(1)
        if name is None or name == "":
            name = "Other"

        amount = project['Metrics']['BlendedCost']['Amount']
        amount = float(amount)
        line = "{}\t${:,.2f}".format(name, amount)
        print(line)
        tsv_lines.append(line)
        total_cost = total_cost+amount
    tsv_lines.append('\nBy Service: \n')

    print ('\nBy Service: \n')
    for project in response1["ResultsByTime"][0]["Groups"]:
        namestring = project['Keys'][0]
        name = re.search("\$(.*)", namestring).group(1)
        if name is None or name == "":
            name = "Other"

        amount = project['Metrics']['BlendedCost']['Amount']
        amount = float(amount)
        line = "{}\t${:,.2f}".format(name, amount)
        print(line)
        tsv_lines.append(line)
    tsv_lines.append('\nBy Stack: \n')

    print ('\nBy Stack: \n')
    for project in response2["ResultsByTime"][0]["Groups"]:
        namestring = project['Keys'][0]
        name = re.search("\$(.*)", namestring).group(1)
        if name is None or name == "":
            name = "Other"

        amount = project['Metrics']['BlendedCost']['Amount']
        amount = float(amount)
        line = "{}\t${:,.2f}".format(name, amount)
        print(line)
        tsv_lines.append(line)

    send_email(reporttime, "\n".join(tsv_lines),str(round(total_cost,2)))
    print('\nTotal Daily Cost: $'+str(round(total_cost,2)))



def send_email(reporttime, attachment, total_cost):
    print_attachment_in_email = '\n'+'\n'+attachment
    msg = MIMEMultipart()
    msg['From']  = "AWS Admin <aws-admin@domain.com>"
    msg['To'] = "aws.monitoring@domain.com"
    msg['Subject'] = "Daily AWS Cost Breakdown: {}".format(reporttime)

    # what a recipient sees if they don't use an email reader
    msg.preamble = 'Multipart message.\n'

    # the message body
    part = MIMEText('Here is the aws billing data from yesterday.\n\nTotal Daily Cost: $' + total_cost + print_attachment_in_email)
    msg.attach(part)

    # the attachment
    part = MIMEApplication(attachment)
    part.add_header('Content-Disposition', 'attachment', filename="AWS-DailyCostByClient-{}.tsv".format(reporttime))
    msg.attach(part)

    # Create an AWS Simple Email Service (SES) client
    client = boto3.client('ses')

    try:
        response = client.send_raw_email(
            RawMessage={
                 'Data': msg.as_string(),
            },
            #Source=msg['From'],
            #Destinations=to_emails
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['ResponseMetadata']['RequestId'])



if __name__ == "__main__":
    lambda_handler({}, {})

