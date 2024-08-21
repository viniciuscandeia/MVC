
from src.views.people_register_view import PeopleRegisterView
from src.controllers.people_register_controller import PeopleRegisterController


def people_register_constructor():
    people_register_view = PeopleRegisterView()
    people_register_controller = PeopleRegisterController()

    new_person_information = people_register_view.registry_person_view()
    response = people_register_controller.register(new_person_information)

    if response['Sucess']:
        people_register_view.registry_person_sucess(response['Message'])
    else:
        people_register_view.registry_person_failure(response['Error'])
