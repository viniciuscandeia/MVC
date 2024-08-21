from typing import List

from src.models.entities.person import Person


class __PersonRepository:
    def __init__(self) -> None:
        self.__people: List[Person] = []

    def registry_person(self, person: Person) -> None:
        self.__people.append(person)

    def find_person_by_name(self, name: str) -> Person:
        for person in self.__people:
            if person.name == name:
                return person
        return None


person_repository = __PersonRepository()
