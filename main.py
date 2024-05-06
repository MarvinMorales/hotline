from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from sqlmodel import SQLModel

from app.models.connection import engine
from app.routes.root_route import root_router
from app.routes.test_route import test_router
from app.routes.twilio_handle_call_route import twilio_call_handler
from app.routes.twilio_process_response_route import twilio_process_response

prefix = "/api"
app = FastAPI(docs_url="/docs")

SQLModel.metadata.create_all(engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def redirect_root():
    return RedirectResponse(url=prefix)


app.include_router(root_router, prefix=prefix)
app.include_router(test_router, prefix=prefix)
app.include_router(twilio_call_handler, prefix=prefix)
app.include_router(twilio_process_response, prefix=prefix)
