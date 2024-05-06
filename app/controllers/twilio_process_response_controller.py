from os import getenv

from dotenv import load_dotenv
from twilio.twiml.voice_response import VoiceResponse

from app.utils.twilio_make_connection import twilio_client

load_dotenv()


class Controller(object):
    twilio_phone_number = "TU_NUMERO_DE_TELEFONO_TWILIO"

    def __init__(self, message: str):
        # Crear un cliente de Twilio
        self.client = twilio_client
        self.message = message
