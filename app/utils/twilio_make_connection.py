from os import getenv

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()


class Twilio_Client(object):
    def __init__(self):
        self.twilio_client = Client(getenv("TWILIO_SID"), getenv("TWILIO_AUTH_TOKEN"))
