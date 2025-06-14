import requests
import os
import datetime as dt

def create_user(username):
    PIXELA_ENDPOINT = "https://pixe.la/v1/users"
    pixela_params = {
        "token":os.environ.get("PIXELA_TOKEN"),
        "username":username,
        "agreeTermsOfService": "yes",
        "notMinor":"yes",
    }
    response = requests.post(url=PIXELA_ENDPOINT, json=pixela_params)
    print(response.text)
#create_user('skeane')

def create_graph(username):
    PIXELA_ENDPOINT = f"https://pixe.la/v1/users/{username}/graphs"
    headers = {"X-USER-TOKEN":os.environ.get("PIXELA_TOKEN")}
    params = {
        "id":"python-coding",
        "name":"100 days of Code",
        "unit":"commit",
        "type":"int",
        "color":"shibafu",
        "timezone":"America/Chicago",
        "isSecret": False,
        "publishOptionalData": True
    }
    response = requests.post(url=PIXELA_ENDPOINT,headers=headers,json=params)
    print(response.status_code)

#create_graph("skeane")

def post_value(username, graph_id):
    now = dt.datetime.now()
    PIXELA_ENDPOINT = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}"
    headers = {"X-USER-TOKEN":os.environ.get("PIXELA_TOKEN")}
    params = {
        "date": now.strftime("%Y%m%d"),
        "quantity": "5"
    }
    response = requests.post(url=PIXELA_ENDPOINT,headers=headers,json=params)
    print(response)
    return response

#post_value("skeane","python-coding")

def update_value(username, graph_id,date, qty):
    PIXELA_ENDPOINT = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}/{date}"
    headers = {"X-USER-TOKEN":os.environ.get("PIXELA_TOKEN")}
    params = {
        "quantity": str(qty)
    }
    response = requests.put(url=PIXELA_ENDPOINT,headers=headers,json=params)
    print(response)
    return response

#update_value("skeane","python-coding","20250614",1)

def delete_value(username, graph_id,date):
    PIXELA_ENDPOINT = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}/{date}"
    headers = {"X-USER-TOKEN":os.environ.get("PIXELA_TOKEN")}
    response = requests.delete(url=PIXELA_ENDPOINT,headers=headers)
    print(response)
    return response

delete_value("skeane","python-coding","20250614")

