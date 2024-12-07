import requests

def get_public_ip():
    try:
        # Make a request to an external service to get the public IP address
        response = requests.get('https://api.ipify.org?format=json')
        public_ip = response.json()['ip']
    except Exception as e:
        public_ip = "Unable to get public IP: " + str(e)
    
    return public_ip

if __name__ == "__main__":
    print("Public IP Address:", get_public_ip())
