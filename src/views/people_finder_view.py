
import os
from typing import Dict


class PeopleFinderView:
    def find_person_view(self) -> Dict:
        os.system('cls||clear')

        print('Buscar Pessoa \n\n')
        name = input('Entre com o nome: ')

        person_finder_informations = {
            "name": name
        }

        return person_finder_informations

    def find_person_sucess(self, message: Dict) -> None:
        os.system('cls||clear')

        sucess_message = f'''
            Usuario encontrado com sucesso!

            Tipo: {message['type']}
            Registros: {message['count']}
            Infos:
                Name: {message['infos']['name']}
        '''
        print(sucess_message)

    def find_person_failure(self, error: str) -> None:
        os.system('cls||clear')

        failure_message = f'''
            Falha ao encontrar usuario!

            Erro: {error}
        '''
        print(failure_message)
