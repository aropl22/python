import json
import boto3

client = boto3.client('textract')



def get_kv_map(block_list):
    # get key and value maps
    key_map = {}
    value_map = {}
    block_map = {}
    for block in block_list:
        block_id = block['Id']
        block_map[block_id] = block
        if block['BlockType'] == "KEY_VALUE_SET":
            if 'KEY' in block['EntityTypes']:
                key_map[block_id] = block
            else:
                value_map[block_id] = block

    return key_map, value_map, block_map


def get_kv_relationship(key_map, value_map, block_map):
    kvs = defaultdict(list)
    for block_id, key_block in key_map.items():
        value_block = find_value_block(key_block, value_map)
        key = get_text(key_block, block_map)
        val = get_text(value_block, block_map)
        kvs[key].append(val)
    return kvs


def find_value_block(key_block, value_map):
    for relationship in key_block['Relationships']:
        if relationship['Type'] == 'VALUE':
            for value_id in relationship['Ids']:
                value_block = value_map[value_id]
    return value_block


def get_text(result, blocks_map):
    text = ''
    if 'Relationships' in result:
        for relationship in result['Relationships']:
            if relationship['Type'] == 'CHILD':
                for child_id in relationship['Ids']:
                    word = blocks_map[child_id]
                    if word['BlockType'] == 'WORD':
                        text += word['Text'] + ' '
                    if word['BlockType'] == 'SELECTION_ELEMENT':
                        if word['SelectionStatus'] == 'SELECTED':
                            text += 'X'

    return text


def get_analysis_result(jobid, block_list, next_token):
    if(next_token == None):
        result = client.get_document_analysis(JobId=jobid)
    else:
        result = client.get_docuemtn_analysis(JobId=jobid, NextToken=next_token)
    
    blocks = result.get("Blocks")

    if(blocks !=None):
        block_list.extend(blocks)
        if(result.get("NextToken") != None):
            get_analysis_result(jobid, block_list, result["NextToken"])
    return block_list
            
            
def lambda_handler(event, context):
    #next_token = None
    block_list = []
    try:
        # Extract SNS message
        sns_message = event['Records'][0]['Sns']
        
        # Parse the JSON message
        message_body = json.loads(sns_message['Message'])
        
        # Extract the status from the message
        status = message_body.get('Status', 'Status not found')
        
        if status == "SUCCEEDED":
            jobid =  message_body.get('JobId', 'JobId not found')
            s3_object = message_body.get('DocumentLocation', 'S3_Object_name not found')['S3ObjectName']
            s3_bucket = message_body.get('DocumentLocation', 'S3_Bucket_name not found')['S3Bucket']
            print('JobID: ',jobid)
            print('s3_bucket: ',s3_bucket)
            print('s3_object: ',s3_object)
            block_list = get_analysis_result(jobid, block_list, next_token = None)
            print('Block list: ',get_analysis_result(jobid, block_list, next_token = None))
            
            key_map, value_map, block_map = get_kv_map( bucket, file_name)

    # Get Key Value relationship
            kvs = get_kv_relationship(key_map, value_map, block_map)
            print("\n\n== FOUND KEY : VALUE pairs ===\n")

            for key, value in kvs.items():
                print(key, ":", value)
            
            return {
                'statusCode': 200,
                'body': json.dumps('Message processed successfully')
            }
    
    except KeyError as e:
        print("KeyError:", e)
        print("Event structure or SNS message format might be incorrect.")
        return {
            'statusCode': 400,
            'body': json.dumps('Error processing message')
        }
    except json.JSONDecodeError as e:
        print("JSONDecodeError:", e)
        print("Error decoding JSON message.")
        return {
            'statusCode': 400,
            'body': json.dumps('Error processing message')
        }
