import requests
import json

def getPrice(loadZone):
    request_data_raw = {'settlement_point': loadZone}
    request_data = json.dumps(request_data_raw)
    response_raw = requests.post("https://app.gogriddy.com/api/v1/insights/getnow",data=request_data );
    if response_raw.ok:
        response = response_raw.text
        print(response)
    else:
        print("error getting prices")
