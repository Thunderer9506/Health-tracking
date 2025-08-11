import requests
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
nutri = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety = "https://api.sheety.co/"+os.getenv("SHEETY_URL")+"/healthTracker/sheet1"

ask = input("What you have did today?")

head = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}
para = {
    "query":ask,
}
response_nutri = requests.post(url=nutri,headers=head,json=para)
data = response_nutri.json()
print("Nutritionix response:", data)  # Debug output

# Check if exercises exist
if "exercises" not in data or not data["exercises"]:
    print("No exercises found. Please check your input.")
else:

    now = datetime.now()
    today = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")

    first_exercise = data["exercises"][0]

    para_sheety = {
        "sheet1": {   # Must match your sheet tab name in lowercase
            "date": today,
            "time": time,
            "exercise": first_exercise.get("user_input", ""),
            "duration": first_exercise.get("duration_min", 0),
            "calories": first_exercise.get("nf_calories", 0),
        }
    }
    head = {
        "Authorization":os.getenv("AUTHORIZATION")
    }

    response_sheety = requests.post(url=sheety,json=para_sheety,headers=head)
    print(response_sheety.text)