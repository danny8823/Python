import requests
from twilio.rest import Client
import os

# account_sid = 'AC4e6f6a560a4808a4508e33813e7b2397'
# auth_token = '6482434197af90aed99024895d2e5b43'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#     from_='+18885967774',
#     body='Hello from Twilio',
# )

print(os.environ.get('OWM_API_KEY'))
api_key = 'bd7268718b1d8e8bf47f6f11805dde99'
api_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
weather_params = {
    'lat': 33.824249,
    'lon': 118.045692,
    'appid': api_key,
    'cnt': 4
}

rain = 0

try:
    res = requests.get(api_endpoint, params=weather_params)
    check = res.status_code
    data = res.json()
except:
    print(check)


for num in range(3):
    weather = data['list'][num]['weather'][0]
    if weather['main'] == 'Rain':
        print(data['list'][num].dt_text)
        rain += 1

print(rain)
