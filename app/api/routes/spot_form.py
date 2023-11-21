from fastapi import APIRouter, Request
from app.services.responses import JSONResponse
from app.services.templates_management import (run_search, db_connection,
                                               WebFormTemplate)


router = APIRouter()


@router.post("/spot_form/", status_code=200)
async def spot_web_form(request: Request):
    cont = await request.form()
    if not cont:
        return JSONResponse(
            status_code=200,
            content={"message": "empty form"})
    resp = await run_search(
        con=db_connection, form=cont, converter=WebFormTemplate, ignore="name"
    )
    return resp
