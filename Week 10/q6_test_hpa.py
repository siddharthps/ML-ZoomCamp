import requests
from time import sleep

# Define the URL of the subscription service
url = "http://localhost:9696/predict"

# Define the client data payload
client = {"job": "management", "duration": 400, "poutcome": "success"}

# Loop to continuously send requests
while True:
    try:
        # Send a POST request to the service
        response = requests.post(url, json=client).json()
        # Print the response
        print(response)
        # Sleep for 0.1 seconds between requests to control the load
        sleep(0.1)
    except Exception as e:
        # Catch and log any exceptions (e.g., connection errors)
        print(f"Error: {e}")
        break
