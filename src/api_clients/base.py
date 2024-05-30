from abc import ABC, abstractmethod
from src.dto import Vacancy


class VacancyApiClient(ABC):
    """
    Представляет общие требования к будущим классам,
    реализующим функционал взаимодействия с API.
    """

    @abstractmethod
    def get_vacancies(self, search_text: str) -> list[Vacancy]:
        pass
