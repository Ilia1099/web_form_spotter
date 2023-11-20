from .test_wfs_client import test_app
import pytest


def test_spotter_filled_form_templ_not_exists():
    with test_app as tc:
        data = {
            "f_name": "ilya",
            "surname": "plat",
            "cur_date": "20.11.2023",
            "phone_num": "+7 916 000 00 00"
        }
        expected_templ = {
            "f_name": "text",
            "surname": "text",
            "cur_date": "datetime",
            "phone_num": "phone"
        }
        response = tc.post(
            url="/spot_form/",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=data
        )
        cont = response.json()
        message = cont.get("message")
        templ = cont.get("template")
        assert response.status_code == 200
        assert templ == expected_templ
        assert message == ("suitable template was not found here is a "
                           "possible one")


def test_spotter_empty_form():
    with test_app as tc:
        data = {}
        response = tc.post(
            url="/spot_form/",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=data
        )
        cont = response.json()
        message = cont.get("message")
        assert response.status_code == 204
        assert message == "empty form"


def test_spotter_req_missing_header():
    with test_app as tc:
        data = {}
        response = tc.post(
            url="/spot_form/",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=data
        )
        cont = response.json()
        message = cont.get("message")
        assert response.status_code == 204
        assert message == "empty form"


def test_spotter_filled_form_templ_exists():
    with test_app as tc:
        data = {
            "full_name": "Hue Jackman",
            "phone_num": "+7 900 000 00 00"
        }
        response = tc.post(
            url="/spot_form/",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=data
        )
        cont = response.json()
        message = cont.get("message")
        templ_name = cont.get("name")
        assert response.status_code == 200
        assert message == "suitable template was found"
        assert templ_name == "SimpleTemplate"
