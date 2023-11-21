from functools import reduce
from typing import Type
from starlette.datastructures import FormData
from app.serializers.form_serializers import WebFormTemplate
from app.database.connection import db_connection
from .responses import templ_was_found, templ_was_not_found
from tinydb import where


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
        form_dict: dict, con: Type[db_connection], ignore: str
) -> dict | None:
    """
    A coroutine which runs a db query to check if sufficient template
    already exists
    :param form_dict: a dictionary which represents a template of provided
    form
    :param ignore: field which should be ignored, by default 'name' because
    it was specified as field for template's name
    :param con TinyDB connection instance
    :return: dictionary of either found template's name
    or currently created template for the provided form
    """
    fields = [key for key in form_dict.keys() if key != ignore]
    conditions = [(where(k) == form_dict.get(k)) for k in fields]
    matches = con.search(reduce(lambda x, y: x & y, conditions))
    for temp in matches:
        template_set = set(temp.keys())
        template_set.remove("name")
        form_set = set(form_dict.keys())
        if template_set.issubset(form_set):
            return temp


async def run_search(
        con: Type[db_connection], form: FormData,
        converter: Type[WebFormTemplate], ignore: str = "name"
):
    template = await get_form_template(form, converter)
    exists = await check_templ_exists(template, con, ignore)
    if exists:
        resp = await templ_was_found(exists.get(ignore))
        return resp
    resp = await templ_was_not_found(template)
    return resp
