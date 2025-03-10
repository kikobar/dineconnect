import requests
import json
from config import *
from delete import *
import sys
import base64

def delete_tickets():
    from_date = str(input('From date [YYYY-MM-DD]: ') or "")
    to_date = str(input('To date YYYY-MM-DD]: ') or "")
    query_filter = json.dumps({
        "businessDate": {'$gte': from_date+"T00:00:00", '$lte': to_date+"T00:00:00"}
        })
    print(query_filter)
    delete(query_filter)
     
if __name__ == '__main__':
    delete_tickets()
    
