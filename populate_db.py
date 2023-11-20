from app.database.connection import db_connection


def add_template_to_db(templ: dict, con=db_connection):
    print(id(con))
    con.insert(templ)


def construct_template():
    name = input("Enter template name: ")
    form = {"name": name}
    amount_of_fields = int(input("Enter number of fields: "))
    for _ in range(amount_of_fields):
        field_name = input("Enter field's name: ")
        flag = field_name in form
        while flag:
            ovrd = input("Field already exists, override: yes/no?: ").lower()
            if ovrd == "no":
                field_name = input("Enter field's name: ").lower()
                flag = field_name in form
            if ovrd == "yes":
                break
        field_value = input(f"Enter type for {field_name}: ").lower()
        form[field_name] = field_value
    return form


def main():
    starting_prompt = input("Add a template? yes/no: ").lower()
    if starting_prompt == "no":
        return -1
    while True:
        templ = construct_template()
        add_template_to_db(templ)
        cont = input("Add another one? yes/no: ").lower()
        if cont == "no":
            break


if __name__ == "__main__":
    main()
