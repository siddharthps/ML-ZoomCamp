import requests

url = "http://localhost:8080/predict"
client = {"job": "management", "duration": 400, "poutcome": "success"}

try:
    response = requests.post(url, json=client)
    print("Response:", response.json())
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
