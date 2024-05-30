from abc import ABC, abstractmethod
from src.dto import Vacancy


class FileConnector(ABC):
    """
    Представляет общие требования к будущим классам,
    реализующим взаимодействия программы с набором данных вакансий.
    """

    @abstractmethod
    def get_vacancies(self) -> list[Vacancy]:
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def delete_vacancies(self, vacancy: Vacancy) -> None:
        pass
