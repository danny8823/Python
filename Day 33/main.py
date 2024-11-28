import requests
lat = 0
lng = 0
date = 0


def get_it(lat, lng, date):
    url_response = requests.get(
        url=f'https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&date={date}')
    data = url_response.json()
    print(data)


get_it(lat=33.811470913954025, lng=-118.04348823340797, date='today')
