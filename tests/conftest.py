import pytest
from pathlib import Path
from src.dto import Vacancy, Salary
from src.file_connector import JSONConnector


@pytest.fixture
def json_connector():
    base_path = Path(__file__).parent
    vacancies_path_file = base_path.joinpath("vacancies.json")
    return JSONConnector(vacancies_path_file)


@pytest.fixture
def v1():
    return Vacancy(
        name="v1",
        url="https://api.hh.ru/vacancies/1",
        employer_name="DD",
        salary=Salary(currency="RUR", salary_from=100, salary_to=500)
    )


@pytest.fixture
def v2():
    return Vacancy(
        name="v2",
        url="https://api.hh.ru/vacancies/2",
        employer_name="DD",
        salary=Salary(currency="RUR", salary_from=200, salary_to=500)
    )


@pytest.fixture
def v3():
    return Vacancy(
        name="v3",
        url="https://api.hh.ru/vacancies/3",
        employer_name="DD",
        salary=Salary(currency="RUR", salary_from=None, salary_to=5000)
    )


@pytest.fixture
def vacancies(v1, v2, v3):
    return [v1, v2, v3]
