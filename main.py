import requests, json, time 
from requests.exceptions import HTTPError 

url = "http://172.16.10.164/api/portal/app_save_application.php"
headers = {"Content-Type" : "application/json; charset=utf-8"}

with open("op.json", "r") as file:
    datas = file.readlines()
    for i in range(len(datas)):
        print(json.loads(datas[i]))
        try:
            print(f"\nPosting {i + 1} of {len(datas)}")
            print(f"\nData: {json.loads(datas[i])}")
            result = requests.post(url, json = json.loads(datas[i]), headers=headers)
            print(f"\nCode: {result.status_code}, Response: {result.text}")
        except HTTPError as http_error:
            print(f"HTTP Error Occured: {http_error}")
        except Exception as error:
            print(f"\nError Occured: {error}")
        print(f"\nSleeping for 1 Seconds")
        time.sleep(1.5)