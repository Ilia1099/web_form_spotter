from fastapi.responses import JSONResponse,Response


async def templ_was_found(name: str) -> Response:
    """
    Coroutine which prepares response for case when suitable template was found
    :param name: name of the template
    """
    content = {
        "message": "suitable template was found",
        "name": name
    }
    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-store, max-age=0"

    }
    return JSONResponse(content=content, headers=headers)


async def templ_was_not_found(form_dict: dict) -> Response:
    """
    Coroutine which prepares response for case when no template was found
    :param form_dict: templated generated on provided form
    """
    content = {
        "message": "suitable template was not found here is a possible one",
        "template": form_dict
    }
    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-store, max-age=0"

    }
    return JSONResponse(content=content, headers=headers)


