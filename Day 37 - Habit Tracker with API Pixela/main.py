import requests
from datetime import datetime

TOKEN = "TESTE"
USERNAME = "gabdsalles"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Criar usuário
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Criar um grafo
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "coding graph",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Criar um graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_graph_endpoint = f"{graph_endpoint}/graph1"

today = datetime.now()
print(today.strftime("%Y%m%d"))

post_graph_json = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2.0"
}

yesterday = datetime(year=2024, month=1, day=29)

post_graph_yesterday = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "4.0"
}

# Colocar informações no graph
# response = requests.post(url=post_graph_endpoint, json=post_graph_yesterday, headers=headers)
# print(response.text)

yesterday_formatted = yesterday.strftime("%Y%m%d")
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{yesterday_formatted}"

update_pixel_config = {
    "quantity": "3.0"
}

# Atualizar a data de ontem usando HTTP put request
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

# Deletar o pixel de ontem usando HTTP DELETE request
# response = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(response.text)