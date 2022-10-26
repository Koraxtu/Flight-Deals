import requests
from datetime import datetime, timedelta
import os


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url = "https://api.tequila.kiwi.com"
        TEQUILA_KEY = os.environ["TEQUILA_KEY"]
        self.header = {"apikey": TEQUILA_KEY}

    def tester(self, city):
        url = self.url + "/locations/query"
        params = {
            "term": city,
            "limit": 1
        }
        response = requests.get(url=url, headers=self.header, params=params)
        response.raise_for_status()
        result = response.json()
        return result["locations"][0]["code"]

    def pricing(self, city, price):
        today = datetime.today()
        future = today + timedelta(days=180)
        future = future.strftime("%d/%m/%Y")
        today = today.strftime("%d/%m/%Y")
        url = self.url + "/v2/search"
        params = {
            "fly_from": os.environ["LOCAL_AIRPORT"],
            "fly_to": city,
            "date_from": today,
            "date_to": future,
            "fight_type": "round",
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 4,
            "curr": "USD",
            "price_from": 0,
            "price_to": price,
            "limit": 1
        }
        response = requests.get(url=url, headers=self.header, params=params)
        response.raise_for_status()
        result = response.json()
        try:
            return result["data"][0]["price"]
        except IndexError:
            return 999

