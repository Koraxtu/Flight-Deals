from twilio.rest import Client
import os


class NotificationManager:

    def __init__(self):
        self.account_sid = os.environ["TWILIO_SID"]
        self.auth_token = os.environ["TWILIO_AUTH"]
        self.valid_flights = False
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self):
        message = self.client.messages.create(
            body=f"Go check your flight sheet data table",
            from_=os.environ["TWILIO_NUM"],
            to=os.environ["MY_NUM"]
        )
