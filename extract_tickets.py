import requests
import json
from config import *
from push import *
import sys
import base64

def extract_tickets():
    from_date = str(input('From date [YYYY-MM-DD]: ') or "")
    to_date = str(input('To date YYYY-MM-DD]: ') or "")
    url = base_url + "api/Account/Authenticate/"
    payload = json.dumps({
        "tenancyName": api_tenancy_name,
        "usernameOrEmailAddress": api_username,
        "password": api_password
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    bear_token = json.loads(response.text)['result']
    url = base_url + "api/services/app/ticket/GetAllDetailTickets"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+bear_token
    }
    payload = json.dumps({
        "startDate": from_date,
        "endDate": to_date,
        "location": api_location_id
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    tickets = json.loads(response.text)['result']['ticketList']['items']
    for key in tickets:
        print(json.dumps(key))
        push(json.loads(json.dumps(key)))
        
if __name__ == '__main__':
    extract_tickets()
    
