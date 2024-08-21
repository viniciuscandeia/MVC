from .constructor.introduction_process import introduction_process
from .constructor.people_finder_constructor import people_finder_constructor
from .constructor.people_register_constructor import people_register_constructor


def start() -> None:
    while True:
        command = introduction_process()

        match command:
            case '1':
                people_register_constructor()
            case '2':
                people_finder_constructor()
            case '5':
                exit()
            case _:
                print('Comando invalido!')
