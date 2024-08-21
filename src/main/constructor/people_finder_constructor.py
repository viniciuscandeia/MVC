
from src.views.people_finder_view import PeopleFinderView
from src.controllers.people_finder_controller import PeopleFinderController

def people_finder_constructor():
    people_finder_view = PeopleFinderView()
    people_finder_controller = PeopleFinderController()

    people_finder_informations = people_finder_view.find_person_view()
    response = people_finder_controller.find_by_name(people_finder_informations)

    if response['Sucess']:
        people_finder_view.find_person_sucess(response['Message'])
    else:
        people_finder_view.find_person_failure(response['Error'])
