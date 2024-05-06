from twilio.twiml.voice_response import VoiceResponse

from app.utils.json_formatter import Load_Copies
from app.utils.twilio_make_connection import Twilio_Client

language = Load_Copies().data["language"]


class Controller(object):
    def __init__(self, message: list[str]) -> None:
        self.client = Twilio_Client()
        self.message = message

    def make_a_twilio_call_response(self) -> VoiceResponse:
        twiml_response = VoiceResponse()
        twiml_response.say(self.message[0], voice="alice")
        gather = twiml_response.gather(
            num_digits=1, timeout=5, action="/twilio/process-language-selected"
        )
        gather.say(f"{language[0]}, {language[1]}", voice="alice")

        if not gather.children:
            twiml_response.append(gather)

        return twiml_response
