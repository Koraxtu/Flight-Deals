import requests
from pprint import pprint
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.authorization = {"Authorization": os.environ["SHEETY_KEY"], "Content-Type": "application/json"}
        self.url = os.environ["SHEETY_URL"]
        self.result = {}

    def read(self):
        response = requests.get(url=self.url, headers=self.authorization)
        response.raise_for_status()
        self.result = response.json()
        # pprint(self.result)

    def write(self):
        for entry in self.result["prices"]:
            temp_url = f"{self.url}/{entry['id']}"
            body = {"price": {"iataCode": entry["iataCode"]}, "currentPrice": entry["currentPrice"]}
            print(self.authorization)
            response = requests.put(url=temp_url, headers=self.authorization, json=body)
            response.raise_for_status()
            result = response.json()
            pprint(result)
