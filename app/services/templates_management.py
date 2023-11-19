from typing import Type
from starlette.datastructures import FormData
from app.serializers.form_serializers import WebFormTemplate
from app.database import db_connection
from tinydb import Query


async def get_form_template(
        form: FormData, converter: Type[WebFormTemplate]
) -> dict:
    """
    A coroutine which uses WebFormTemplate to parse received form and
    creates a template from it for following usage
    :param form: starlette FormData class with received data
    :param converter: A class for transforming form into template
    :return: dictionary - which represents a template for provided form
    """
    template = converter(form)
    return template.get_template()


async def check_templ_exists(
        form_dict: dict, con=db_connection
) -> dict | None:
    """
    A coroutine which runs a db query to check if sufficient template
    already exists
    :param form_dict: a dictionary which represents a template of provided
    form
    :param con TinyDB connection instance
    :return: dictionary of either found template's name
    or currently created template for the provided form
    """
    matches = con.search(Query().fragment(form_dict))
    if matches:
        return matches[0]
