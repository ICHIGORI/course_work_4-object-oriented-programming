from dataclasses import dataclass


@dataclass
class Salary:
    currency: str | None = None
    salary_from: int | None = None
    salary_to: int | None = None


@dataclass
class Vacancy:
    name: str
    url: str
    employer_name: str
    salary: Salary
