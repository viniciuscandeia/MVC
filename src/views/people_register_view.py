
import os
from typing import Dict


class PeopleRegisterView:
    def registry_person_view(self) -> Dict:
        os.system('cls||clear')

        print('Cadastrar Nova Pessoa \n\n')
        name = input('Entre com o nome: ')
        age = input('Entre com a idade: ')
        height = input('Entre com a altura: ')

        new_person_informations = {
            "name": name,
            "age": age,
            "height": height,
        }

        return new_person_informations

    def registry_person_sucess(self, message: Dict) -> None:
        os.system('cls||clear')

        sucess_message = f'''
            Usuario cadastrado com sucesso!

            Tipo: {message['type']}
            Registros: {message['count']}
            Infos:
                Nome: {message['attributes']['name']}
                Idade: {message['attributes']['age']}
        '''
        print(sucess_message)

    def registry_person_failure(self, error: Dict) -> None:
        os.system('cls||clear')

        failure_message = f'''
            Falha ao cadastrar usuario!

            Erro: {error}
        '''
        print(failure_message)
