import requests
from bs4 import BeautifulSoup

def crawl_webpage(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract information from the webpage
        # For example, let's extract all the links (anchor tags) from the webpage
        links = soup.find_all('a')
        
        # Print out the extracted links
        for link in links:
            print(link.get('href'))
    else:
        print(f"Failed to crawl webpage. Status code: {response.status_code}")

# Example usage:
url = "https://test.com"
crawl_webpage(url)