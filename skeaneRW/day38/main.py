from dotenv import load_dotenv
import os
import requests
import json
import datetime as dt
load_dotenv()

def parse_activity(user_input):
    NUTRITION_ID=os.environ.get("NUTRITION_ID")
    NUTRITION_KEY=os.environ.get("NUTRITION_KEY")
    NUTRITION_ENDPOINT = "https://trackapi.nutritionix.com//v2/natural/exercise"
    headers = {
    "Content-Type": 'application/json',
    "x-app-id": NUTRITION_ID,
    "x-app-key": NUTRITION_KEY 
    }
    params = {
        "query": user_input
    }
    response = requests.post(url=NUTRITION_ENDPOINT,headers=headers,json=params)
    print(response.json())
    if (response.status_code == 200):
        exercises = response.json()["exercises"]
        today = dt.datetime.now()
        entries = []
        for activity in exercises:
            entry = {
                "date": today.strftime('%m/%d/%Y'),
                "time": today.strftime('%H:%M:%S'), 
                "exercise": activity["name"],
                "duration": int(activity["duration_min"]),
                "calories": int(activity["nf_calories"]),
                }
            entries.append(entry)
        return entries

def read_sheet(sheet_name):
    SHEETY_ENDPOINT = f"https://api.sheety.co/9a516cd045dc7d27b3214b91facb73a8/myWorkouts/{sheet_name}"
    SHEETY_KEY = os.environ.get("SHEETY_KEY")
    headers = { "Authorization": f"Bearer {SHEETY_KEY}" }
    response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
    content = response.json()
    print(json.dumps(content))

def post_activity(sheet_name):
    SHEETY_ENDPOINT=f"https://api.sheety.co/9a516cd045dc7d27b3214b91facb73a8/myWorkouts/{sheet_name}"
    SHEETY_KEY = os.environ.get("SHEETY_KEY")
    headers = { "Authorization": f"Bearer {SHEETY_KEY}" }
    activities = parse_activity(input("what did you do?"))
    for activity in activities:
        params={"workout": activity}
        response = requests.post(url=SHEETY_ENDPOINT, headers=headers, json=params)
        print(response.json())

post_activity("workouts")

#read_sheet('workouts')