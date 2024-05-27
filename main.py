from src.api_clients import HeadHunterAPI
from src.api_clients.base import VacancyApiClient


api_client: VacancyApiClient = HeadHunterAPI()


def main():
    vacancies = api_client.get_vacancies('python')
    for i, vacancy in enumerate(vacancies):
        print(vacancy)
        if i >= 4: break


if __name__ == "__main__":
    main()
