from typing import Dict
import asyncio 
import os 
from os.path import join, dirname
from datetime import datetime 
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

from utils import send_telegram_message

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

router = APIRouter(prefix="/backend", tags=[""])

ALERT_SENT = False

async def reset_alert():
    global ALERT_SENT
    await asyncio.sleep(60)
    ALERT_SENT = False

@router.post("/sendwarning")
async def read_output(trigger: Dict[str, str]):
    global ALERT_SENT
    if not ALERT_SENT:
        if trigger["message"] == "Fall Down":
            ALERT_SENT = True
            send_telegram_message(bot_token=BOT_TOKEN, chat_id=CHAT_ID,
                                  message=f"Alerta. Queda detectada em {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
            asyncio.create_task(reset_alert())
            return JSONResponse(content={"message": "Alert sended to Telegram"}, status_code=200)
        else:
            return JSONResponse(content={"error": "Invalid trigger"}, status_code=400)
    else:
        return JSONResponse(content={"message": "Alert already sent"})