import json
from pathlib import Path
from .base import FileConnector
from ..dto import Vacancy, Salary


class JSONConnector(FileConnector):
    """
    Получает, сохраняет, удаляет наборы данных вакансий,
    используя формат JSON
    """

    def __init__(self, file_path: Path, encoding: str = "utf-8"):
        self.__file_path = file_path
        self.encoding = encoding

    def _save(self, *vacancies: Vacancy) -> None:
        """
        Сохраняет вакансии в файл"""

        data = [self._parse_vacancy_to_dict(vacancy) for vacancy in vacancies]
        with self.__file_path.open('w', encoding=self.encoding) as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    @staticmethod
    def _parse_vacancy_to_dict(vacancy: Vacancy) -> dict:
        """
        Парсит данные вакансии и приводит их к формату словаря"""

        return {
            "name": vacancy.name,
            "url": vacancy.url,
            "employer_name": vacancy.employer_name,
            "salary": {
                "from": vacancy.salary.salary_from,
                "to": vacancy.salary.salary_to,
                "currency": vacancy.salary.currency
            }
        }

    @staticmethod
    def _parse_dict_to_vacancy(data: dict) -> Vacancy:
        """
        Парсит данные словаря и создаёт объект вакансии"""

        return Vacancy(
            name=data["name"],
            url=data["url"],
            employer_name=data["employer_name"],
            salary=Salary(
                salary_from=data["salary"]["from"],
                salary_to=data["salary"]["to"],
                currency=data["salary"]["currency"]
            )
        )

    def get_vacancies(self) -> list[Vacancy]:
        """
        Возвращает список вакансий из файла"""

        if not self.__file_path.exists():
            return []

        vacancies = []
        with self.__file_path.open(encoding=self.encoding) as file:
            for item in json.load(file):
                vacancy = self._parse_dict_to_vacancy(item)
                vacancies.append(vacancy)

        return vacancies

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Сохраняет вакансии в файл, если их там ранее не было"""

        vacancies = self.get_vacancies()
        if vacancy not in vacancies:
            vacancies.append(vacancy)
            self._save(*vacancies)

    def delete_vacancies(self, vacancy: Vacancy) -> None:
        """
        Удаляет вакансию из файла, если она там ранее была"""

        vacancies = self.get_vacancies()
        if vacancy in vacancies:
            vacancies.remove(vacancy)
            self._save(*vacancies)
