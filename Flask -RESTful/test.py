import requests
import json

# URL BASE(route)
# Test - GET AN User - Route = 'http://127.0.0.1:5000/pessoa/Alex'
# url = 'http://127.0.0.1:5000/pessoa/Alex'
# x = requests.get(url)
# res = json.loads(x.text)
# print(res)

# Test - GET (ALL DATA) - [ROUTE = 'http://127.0.0.1:5000/pessoa/']
url = 'http://127.0.0.1:5000/pessoa/'
x = requests.get(url)
res = json.loads(x.text)
print(res)

# Test POST
# url = 'http://127.0.0.1:5000/pessoa/'
# payload = {'nome': "Tomas Jerry", 'idade': 22}
# x = requests.post(url, json=payload)
# res = json.loads(x.text)
# print(res)

# # Test DELETE
# url = 'http://127.0.0.1:5000/pessoa/Tomas Jerry'
# x = requests.delete(url)
# #print(x.text)
# print(json.loads(x.content))

