import requests
from src.api_clients import HeadHunterAPI
from src.dto import Vacancy, Salary


class TestHeadHunterAPI:

    def test__parse_vacancy_data(self):
        response = requests.Response()
        content = (b'{"items":[{"id":"100374416","premium":false,'
                   b'"name":"\xd0\xa0\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x87\xd0\xb8\xd0\xba '
                   b'\xd0\xbc\xd0\xbe\xd0\xb1\xd0\xb8\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe '
                   b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xbb\xd0\xbe\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f '
                   b'\xd0\xbd\xd0\xb0 iOS (\xd0\xb8\xd0\xbd\xd0\xb4\xd0\xb8-\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0'
                   b'\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0)","department":null,"has_test":false,'
                   b'"response_letter_required":false,"salary":{"from":1000000,"to":3500000,"currency":"KZT",'
                   b'"gross":true},"url":"https://api.hh.ru/vacancies/100374416?host=hh.ru", "relations":[],'
                   b'"employer":{"id":"5969916",'
                   b'"name":"\xd0\xa4\xd0\xb8\xd0\xbd\xd0\xb4\xd0\xb8\xd1\x80\xd0\xb5\xd0\xba\xd1\x86\xd0\xb8\xd1\x8f'
                   b'","url":"https://api.hh.ru/employers/5969916",'
                   b'"alternate_url":"https://hh.ru/employer/5969916"}}]}')

        vacancy = Vacancy("Разработчик мобильного приложения на iOS (инди-разработка)",
                          "https://api.hh.ru/vacancies/100374416?host=hh.ru",
                          "Финдирекция",
                          Salary("KZT",
                                 1000000,
                                 3500000
                                 )
                          )

        response._content = content
        assert HeadHunterAPI._parse_vacancy_data(response) == [vacancy]
