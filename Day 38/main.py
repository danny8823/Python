import requests
import os
from datetime import datetime

os.environ['nutritionix-api-endpoint'] = 'https://trackapi.nutritionix.com/v2/natural/exercise'
print(os.environ['nutritionix-api-endpoint'])
APP_ID = '2b71eaf0'
APP_KEY = 'fe3d4b431a8699ced359d8200d8cf1d3'
API_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETS_URL = 'https://api.sheety.co/dd53994069e761c9fb2443b1987496b4/myWorkouts/workouts'


headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY
}

sheet_headers = {
    'Authorization': 'Bearer hihi'
}
query = input('What exercise did you do today?')

parameters = {
    'query': query,
    'gender': 'male'

}

response = requests.post(API_ENDPOINT, headers=headers, json=parameters)

workout_data = response.json()

calories = workout_data['exercises'][0]['nf_calories']
duration = workout_data['exercises'][0]['duration_min']
exercise = workout_data['exercises'][0]['user_input']
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

print(calories, duration, exercise)
print(time)

body = {
    'workout': {
        'date': date,
        'time': time,
        'exercise': exercise.title(),
        'duration': int(duration),
        'calories': int(calories)

    }
}
get_sheets = requests.post(SHEETS_URL, json=body, headers=sheet_headers)
print(get_sheets)
