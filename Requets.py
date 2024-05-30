import requests

response = requests.post("http://127.0.0.1:8000/record", json={"engine_temperature": 0.69})
print(response.json())
# response = requests.post("http://127.0.0.1:8000/record", json={"engine_temperature": 0.5})
# print(response.json())
# response = requests.post("http://127.0.0.1:8000/record", json={"engine_temperature": 0.2})
# print(response.json())

response2 = requests.post("http://127.0.0.1:8000/collect")
print(response2.json())