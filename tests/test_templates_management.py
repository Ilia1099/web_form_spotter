from app.database.connection import db_connection
from app.serializers.form_serializers import WebFormTemplate
from app.services.templates_management import (get_form_template,
                                           check_templ_exists)
import pytest
import asyncio
from .test_form_serializer import FormData


not_null_form = [
    {
        "case":
            (
                ('name', 'ilya'), ('phone', '+7 916 229 37 70'),
                ('date', '2023-11-15')
            ),
        "result": {"name": 'text', "phone": 'phone', "date": 'datetime'}
     },
    {
        "case":
            (
                ('name', 'ilya'), ('phone', '+7 916 229 37 70'),
                ('date', '2023-11-45')
            ),
        "result": {"name": 'text', "phone": 'phone', "date": 'text'}
    },
    {
        "case":
            (
                ('name', 'ilya'), ('phone', '+7 916 229 37 7000'),
                ('date', '2023-11-45')
            ),
        "result": {"name": 'text', "phone": 'text', "date": 'text'}
    }
]


@pytest.mark.asyncio
async def test_get_form_template_ok():
    for tc in not_null_form:
        test_case = tc.get("case")
        expected_res = tc.get("result")
        form = FormData(test_case)

        templ = await get_form_template(form, WebFormTemplate)
        assert isinstance(templ, dict)
        for key, val in templ.items():
            assert expected_res[key] == val


@pytest.mark.asyncio
async def test_check_templ_exists_ok():
    data = (("full_name", "Hue Jackman"),
            ("phone_num", "+7 900 000 00 00"))
    form = FormData(data)
    templ = await get_form_template(form, WebFormTemplate)
    exists = await check_templ_exists(templ, db_connection, "name")
    assert exists


@pytest.mark.asyncio
async def test_check_templ_exists_no_templ():
    data = (('phone_num', '+7 916 229 37 70'),
            ('name', "kkk"))
    form = FormData(data)
    templ = await get_form_template(form, WebFormTemplate)
    exists = await check_templ_exists(templ, db_connection, "name")
    assert not exists
