import pytest
from src.dto import Salary, Vacancy


class TestSalary:

    equal_1 = [
        [{"salary_from": None, "salary_to": None}, {"salary_from": None, "salary_to": None}],
        [{"salary_from": None, "salary_to": 110}, {"salary_from": None, "salary_to": 110}],
        [{"salary_from": 100, "salary_to": None}, {"salary_from": 100, "salary_to": None}],
        [{"salary_from": 100, "salary_to": 110}, {"salary_from": 100, "salary_to": 110}],
    ]

    equal_2 = [
        [{"salary_from": 100, "salary_to": None}, {"salary_from": 100, "salary_to": 110}],
        [{"salary_from": None, "salary_to": 110}, {"salary_from": 100, "salary_to": 110}],
        [{"salary_from": 100, "salary_to": 110}, {"salary_from": 100, "salary_to": None}],
        [{"salary_from": 100, "salary_to": 110}, {"salary_from": None, "salary_to": 110}],
    ]

    inequality = [
        [{"salary_from": None, "salary_to": None}, {"salary_from": 100, "salary_to": None}],
        [{"salary_from": None, "salary_to": None}, {"salary_from": None, "salary_to": 110}],
        [{"salary_from": None, "salary_to": None}, {"salary_from": 100, "salary_to": 110}],
        [{"salary_from": 100, "salary_to": None}, {"salary_from": None, "salary_to": None}],
        [{"salary_from": 100, "salary_to": None}, {"salary_from": None, "salary_to": 110}],
        [{"salary_from": None, "salary_to": 110}, {"salary_from": None, "salary_to": None}],
        [{"salary_from": None, "salary_to": 110}, {"salary_from": 100, "salary_to": None}],
        [{"salary_from": 100, "salary_to": 110}, {"salary_from": None, "salary_to": None}],
    ]

    less = [
        [{"salary_from": None, "salary_to": None}, {"salary_from": 100, "salary_to": None}],
        [{"salary_from": None, "salary_to": None}, {"salary_from": None, "salary_to": 110}],
        [{"salary_from": None, "salary_to": None}, {"salary_from": 100, "salary_to": 110}],
        [{"salary_from": 100, "salary_to": None}, {"salary_from": 101, "salary_to": None}],
        [{"salary_from": None, "salary_to": 110}, {"salary_from": None, "salary_to": 111}],
        [{"salary_from": 100, "salary_to": 110}, {"salary_from": 101, "salary_to": 111}],
    ]

    more = [
        [{"salary_from": 101, "salary_to": 111}, {"salary_from": None, "salary_to": None}],
        [{"salary_from": 101, "salary_to": None}, {"salary_from": None, "salary_to": None}],
        [{"salary_from": None, "salary_to": 111}, {"salary_from": None, "salary_to": None}],
        [{"salary_from": 101, "salary_to": None}, {"salary_from": 100, "salary_to": None}],
        [{"salary_from": 101, "salary_to": 111}, {"salary_from": 100, "salary_to": None}],
        [{"salary_from": None, "salary_to": 111}, {"salary_from": None, "salary_to": 110}],
        [{"salary_from": 101, "salary_to": 111}, {"salary_from": None, "salary_to": 110}],
        [{"salary_from": 101, "salary_to": 111}, {"salary_from": 100, "salary_to": 110}],
    ]

    @pytest.mark.parametrize("equal", equal_1)
    def test_equal_1(self, equal):
        salary_1 = Salary(currency='RUB', **equal[0])
        salary_2 = Salary(currency='RUB', **equal[1])

        assert salary_1 == salary_2

    @pytest.mark.parametrize("equal", equal_2)
    def test_equal_2(self, equal):
        salary_1 = Salary(currency='RUB', **equal[0])
        salary_2 = Salary(currency='RUB', **equal[1])

        assert salary_1 == salary_2

    @pytest.mark.parametrize("inequality", inequality)
    def test_inequality(self, inequality):
        salary_1 = Salary(currency='RUB', **inequality[0])
        salary_2 = Salary(currency='RUB', **inequality[1])

        assert salary_1 != salary_2

    @pytest.mark.parametrize("less", less)
    def test_less(self, less):
        salary_1 = Salary(currency='RUB', **less[0])
        salary_2 = Salary(currency='RUB', **less[1])

        assert salary_1 < salary_2

    @pytest.mark.parametrize("less_or_equal", equal_1 + equal_2 + less)
    def test_less_or_equal(self, less_or_equal):
        salary_1 = Salary(currency='RUB', **less_or_equal[0])
        salary_2 = Salary(currency='RUB', **less_or_equal[1])

        assert salary_1 <= salary_2

    @pytest.mark.parametrize("more", more)
    def test_more(self, more):
        salary_1 = Salary(currency='RUB', **more[0])
        salary_2 = Salary(currency='RUB', **more[1])

        assert salary_1 > salary_2

    @pytest.mark.parametrize("more_or_equal", equal_1 + equal_2 + more)
    def test_more_or_equal(self, more_or_equal):
        salary_1 = Salary(currency='RUB', **more_or_equal[0])
        salary_2 = Salary(currency='RUB', **more_or_equal[1])

        assert salary_1 >= salary_2


class TestVacancy:

    def test_sort_top(self, vacancies):
        assert sorted(vacancies, key=lambda x: x.salary, reverse=True) == vacancies[::-1]
