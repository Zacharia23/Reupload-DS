import concurrent.futures
import threading
import json
from time import time, sleep
from pprint import pprint
from requests import Session
from requests.exceptions import HTTPError

url = "http://172.16.10.164/api/portal/app_save_application.php"
headers = {"Content-Type": "application/json; charset=utf-8"}
thread_local = threading.local

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = Session()
        thread_local.session.headers = headers
    return thread_local.session

def post_data(data):
    session = get_session()
    try:
        print(f"\nPosting {datas.index(data) + 1} of {len(datas)}")
    except ValueError:
        print(f"\nData: {data} not found in list")
    pprint(f"\nData: {json.loads(data)}")
    with session.post(url, json=json.loads(data)) as res:
        print(f"\nCode: {res.status_code}, Response: {res.text}")
        print(f"\nSleeping for 1 second ------------------")
        sleep(1)

def post_all_data(datas):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(post_data, datas)

with open("output.json", "r") as file:
    datas = file.readlines
    start = time()
    post_all_data(datas)
    duration = time() - start
    print(f"Posted {len(datas)} data in {duration/60} minutes")

