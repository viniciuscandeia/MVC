from typing import Dict

from src.models.entities.person import Person
from src.models.repository.person_repository import person_repository


class PeopleFinderController:
    def find_by_name(self, people_finder_informations: Dict) -> Dict:
        try:
            self.__validate_fields(people_finder_informations)
            person = self.__find_person(people_finder_informations)
            response = self.__format_response(person)
            return {"Sucess": True, "Message": response}
        except Exception as exception:
            return {"Sucess": False, "Error": str(exception)}

    def __validate_fields(self, people_finder_informations: Dict) -> None:
        if not isinstance(people_finder_informations["name"], str):
            raise Exception("Campo Nome Invalido!")

    def __format_response(self, person: Person) -> Dict:
        return {
            "count": 1,
            "type": "Person",
            "infos": {
                "name": {person.name},
                "age": {person.age},
                "height": {person.height},
            },
        }

    def __find_person(self, person_finder_informations: Dict) -> Person:
        name: str = person_finder_informations["name"]
        person = person_repository.find_person_by_name(name)
        if not person:
            raise Exception("Pessoa nao encontrada!")
        return person
