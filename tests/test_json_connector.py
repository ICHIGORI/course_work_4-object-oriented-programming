import pytest


class TestJSONConnector:

    def test_add_vacancies(self, json_connector, vacancies):
        for v in vacancies:
            json_connector.add_vacancy(v)

    def test_get_vacancies(self, json_connector, vacancies):
        file_vacancies = json_connector.get_vacancies()
        assert file_vacancies == vacancies

    def test_delete_vacancy(self, json_connector, v1, v2, v3):
        json_connector.delete_vacancies(v3)
        file_vacancies = json_connector.get_vacancies()
        assert file_vacancies == [v1, v2]
