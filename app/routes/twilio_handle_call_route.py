from fastapi import APIRouter, Response

from app.controllers.twilio_call_handler_controller import Controller
from app.utils.json_formatter import Load_Copies

twilio_call_handler = APIRouter()

welcome = Load_Copies().data["welcome_data"]["welcome"]


@twilio_call_handler.post("/twilio/call")
async def twilio_call_hanlder_webhook():
    controller = Controller(welcome)
    twiml_response = controller.make_a_twilio_call_response()
    return Response(content=str(twiml_response), media_type="application/xml")
