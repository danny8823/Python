import requests

kanye_api = 'https://api.kanye.rest'

kanye_api_response = requests.get(url=kanye_api)
kanye_quotes_data = kanye_api_response.json()

print(kanye_quotes_data)
