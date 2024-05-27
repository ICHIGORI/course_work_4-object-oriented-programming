from pathlib import Path
from src.api_clients import HeadHunterAPI
from src.api_clients.base import VacancyApiClient
from src.file_connector import JSONConnector
from src.file_connector.base import FileConnector
from src.user_assistant import UserAssistant

BASE_PATH = Path(__file__).parent
VACANCIES_PATH_FILE = BASE_PATH.joinpath("vacancies.json")

api_client: VacancyApiClient = HeadHunterAPI()
json_connector: FileConnector = JSONConnector(VACANCIES_PATH_FILE)

WELCOME_MESSAGE = """Добро пожаловать в программу!\n"""
MENU_MESSAGE = """
Выберите действия:
    1. Загрузит вакансии в файл: по ключевому слову
    2. Вывести топ N вакансий из файла: по зарплате
    0. Выйти
    """

user_assistant = UserAssistant(api_client, json_connector)
MENU = {'1': user_assistant.search_vacancies, '2': user_assistant.show_vacancies}


def main():

    print(WELCOME_MESSAGE)
    while True:
        print(MENU_MESSAGE)
        user_input = input()
        if not user_input.isdigit():
            continue

        if user_input in MENU:
            MENU[user_input]()
        elif user_input == '0':
            break


if __name__ == "__main__":
    main()
