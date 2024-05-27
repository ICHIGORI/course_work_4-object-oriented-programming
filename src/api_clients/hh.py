import requests
from .base import VacancyApiClient
from src.dto import Vacancy, Salary


class HeadHunterAPI(VacancyApiClient):

    def __init__(self, url="https://api.hh.ru/vacancies/", per_page=100):
        self.url = url
        self.per_page = per_page

    def _parse_vacancy_data(self, data: dict) -> Vacancy:
        return Vacancy(
            name=data["name"],
            url=data["url"],
            employer_name=data["employer"]["name"],
            salary=Salary(
                salary_from=data["salary"]["from"],
                salary_to=data["salary"]["to"],
                currency=data["salary"]["currency"]
            )
        )

    def get_vacancies(self, search_text: str) -> list[Vacancy]:
        params = {
            "only_with_salary":  True,
            "per_page": self.per_page,
            "text": search_text
        }

        response = requests.get(self.url, params, timeout=4)
        if not response.ok:
            print(f"Ошибка получения данных с hh.ru, {response.content}")
            return []

        return [
            self._parse_vacancy_data(item)
            for item in response.json()["items"]
        ]


