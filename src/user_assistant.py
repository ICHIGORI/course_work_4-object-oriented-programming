from prettytable import PrettyTable
from src.api_clients.base import VacancyApiClient
from src.file_connector.base import FileConnector


class UserAssistant:
    def __init__(self, api_client: VacancyApiClient, json_connector: FileConnector):
        self.api_client = api_client
        self.json_connector = json_connector

    def search_vacancies(self):
        search_word = input("Введите ключевое слово, для поиска:")
        vacancies = self.api_client.get_vacancies(search_word.lower())
        for vac in vacancies:
            self.json_connector.add_vacancy(vac)

    def show_vacancies(self):
        n = input("Сколько вакансий вывести?\nНе больше 1000\n->")
        if not n.isdigit():
            print("У меня не получилось")
            return None

        n = int(n)

        if (n == 0) or (n > 1000):
            print("У меня не получилось")
            return None

        vacancies = self.json_connector.get_vacancies()

        table = PrettyTable(["name", "url", "employer", "salary"])

        for vacancy in sorted(vacancies, key=lambda x: x.salary, reverse=True)[:n]:
            salary = "{_from} -> {_to}, {currency}".format(
                _from=vacancy.salary.salary_from,
                _to=vacancy.salary.salary_to,
                currency=vacancy.salary.currency
            )
            table.add_row([vacancy.name, vacancy.url, vacancy.employer_name, salary])

        print(table)
