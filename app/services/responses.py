from fastapi.responses import JSONResponse


async def templ_was_found(name: str):
    content = {
        "message": "suitable template was found",
        "name": name
    }
    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-store, max-age=0"

    }
    return JSONResponse(content=content, headers=headers)


async def templ_was_not_found(form_dict: dict):
    content = {
        "message": "suitable template was not found here is a possible one",
        "template": form_dict
    }
    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-store, max-age=0"

    }
    return JSONResponse(content=content, headers=headers)


