
from typing import Dict

class PeopleFinderController:
    def find_by_name(self, people_finder_informations: Dict) -> Dict:
        try:
            self.__validate_fields(people_finder_informations)
            # Buscar em banco de dados
            response = self.__format_response(None)
            return {'Sucess': True, 'Message': response}
        except Exception as exception:
            return {'Sucess': False, 'Error': str(exception)}

    def __validate_fields(self, people_finder_informations: Dict) -> None:
        if not isinstance(people_finder_informations['name'], str):
            raise Exception('Campo Nome Invalido!')

    def __format_response(self, people: any) -> Dict:
        return {
            'count': 1,
            'type': "Person",
            "infos": {
                "name":  "teste"
            }
        }
