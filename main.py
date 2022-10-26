from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

sheet_data = DataManager()
sheet_data.read()
# Check
flightData = FlightSearch()

for entry in sheet_data.result["prices"]:
    entry["iataCode"] = flightData.tester(entry["city"])

# pprint(sheet_data.result)
sheet_data.write()
for entrys in sheet_data.result["prices"]:
    entrys["currentPrice"] = flightData.pricing(entrys["iataCode"], entrys["lowestPrice"])
sheet_data.write()

notifs = NotificationManager()

for line in sheet_data.result["prices"]:
    if line["currentPrice"] <= line["lowestPrice"]:
        notifs.valid_flights = True
if notifs.valid_flights:
    notifs.send_message()
