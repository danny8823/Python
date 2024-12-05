import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = "danny714"
# TOKEN = "lololol123"
# user_params = {
#     "token": "lololol123",
#     "username": "danny714",
#     "agreeTermsofService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url=pixela_endpoint, json=user_params)

# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_config = {
#     "id": "graph1",
#     "name": "Gym graph",
#     "unit": "commit",
#     "type": "float",
#     "color": "ajisai"
# }

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)

# print(response.text)

pixel_add_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.now().strftime('%Y%m%d')

pixel_add_config = {
    'date': '20241205',
    'quantity': '1',
}

# response = requests.post(url=pixel_add_endpoint,
#                          json=pixel_add_config, headers=headers)

# print(response.text)

print(today)

pixel_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}"

pixel_put_config = {
    "quantity": "5"
}

# response = requests.put(url=pixel_put_endpoint,
#                         json=pixel_put_config, headers=headers)

response = requests.delete(f'{pixel_put_endpoint}', headers=headers)

print(response.text)
