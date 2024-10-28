import requests

url = "http://127.0.0.1:9696/predict"
client = {
    "job": "student",
    "duration": 280,
    "poutcome": "failure"
}

try:
    response = requests.post(url, json=client)
    response.raise_for_status()  # Raise an error if the request failed
    print(response.json())
except requests.exceptions.RequestException as e:
    print("Error:", e)