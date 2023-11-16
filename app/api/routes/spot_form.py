from datetime import datetime
from app.serializers.form_serializers import WebFormTemplate
from fastapi import APIRouter, Request



router = APIRouter()


@router.post("/spot_form/", status_code=200)
async def spot_web_form(request: Request):
    cont_type = request.headers.get("Content-Type")
    cont = await request.form()
    cont = cont.items()
    return
