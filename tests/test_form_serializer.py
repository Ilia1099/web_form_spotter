from app.serializers.form_serializers import WebFormTemplate


test_cases = [
    {
        "case":
            (
                ('name', 'ilya'), ('phone', '+7 916 229 37 70'),
                ('date', '2023-11-15')
            ),
        "results": {"name": 'text', "phone": 'phone', "date": 'datetime'}
     },
    {
        "case": [],
        "results": None
    },
    {
        "case":
            (
                ('name', 'ilya'), ('phone', '+7 916 229 37 70'),
                ('date', '2023-11-45')
            ),
        "results": {"name": 'text', "phone": 'phone', "date": 'text'}
    },
    {
        "case":
            (
                ('name', 'ilya'), ('phone', '+7 916 229 37 7000'),
                ('date', '2023-11-45')
            ),
        "results": {"name": 'text', "phone": 'text', "date": 'text'}
    }
]


class FormData:
    def __init__(self, dta):
        self._items = dta

    def items(self):
        return self._items


def test_webformtemplate():
    for tc in test_cases:
        test_case = tc.get("case")
        results = tc.get("results")
        form = FormData(test_case)
        templ_gen = WebFormTemplate(form)
        template = templ_gen.get_template()
        for key, f_type in template.items():
            assert f_type == results[key]


