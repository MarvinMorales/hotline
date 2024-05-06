from fastapi import APIRouter, Form

twilio_process_response = APIRouter()


@twilio_process_response.post("/twilio/process-response")
async def twilio_process_response_webhook(Digits: str = Form(...)):
    print(Digits)
    return Digits
