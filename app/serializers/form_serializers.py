from starlette.datastructures import FormData
from datetime import datetime
from abc import ABC, abstractmethod
import re


class TypeChecker(ABC):
    date_patterns = {
        r"^\d{4}-\d{2}-\d{2}$": "%Y-%m-%d",
        r"^\d{2}\.\d{2}\.\d{4}$": '%d.%m.%Y'
    }
    phone_num_patters = (r'^\+7[ -]?\d{3}[ -]?\d{3}[ -]?\d{2}[ -]?\d{2}$',)
    email_patterns = (r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",)

    @staticmethod
    @abstractmethod
    def is_valid_date(date: str):
        pass

    @staticmethod
    @abstractmethod
    def is_valid_phone_num(num: str):
        pass

    @staticmethod
    @abstractmethod
    def is_valid_email(email: str):
        pass


class FormFieldChecker(TypeChecker):
    @classmethod
    def is_valid_date(cls, date: str) -> str | None:
        for rgx, dform in cls.date_patterns.items():
            if re.fullmatch(rgx, date):
                try:
                    datetime.strptime(date, dform)
                    return "datetime"
                except ValueError:
                    return None

    @classmethod
    def is_valid_phone_num(cls, num: str) -> str | None:
        for rgx in cls.phone_num_patters:
            if re.fullmatch(rgx, num):
                return "phone"

    @classmethod
    def is_valid_email(cls, email: str) -> str | None:
        for rgx in cls.email_patterns:
            if re.fullmatch(rgx, email):
                return "email"

    @classmethod
    def get_field_type(cls, field_value: str):
        checkers = ("is_valid_phone_num", "is_valid_email", "is_valid_date")
        for chk in checkers:
            mthd = getattr(cls, chk)
            field_type = mthd(field_value)
            if field_type:
                return field_type
        return "text"


class WebFormTemplate:
    def __init__(
            self,
            wf: FormData,
            validator: FormFieldChecker = FormFieldChecker
    ):
        self._form: FormData = wf
        self._validator = validator

    def get_template(self):
        template = {}
        for key, val in self._form.items():
            template[key] = self._validator.get_field_type(val)
        return template
