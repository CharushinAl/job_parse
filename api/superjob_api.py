from api.abstract_api import AbstractAPI
from vacancy.vacancy import Vacancy
import requests
import os


class SuperJob(AbstractAPI):

    api: str = os.environ.get("SUPERJOB_API")

    def __init__(self, keyword: str) -> None:
        self.keyword = keyword
        self.__params = {
            'keywords': self.keyword,  # Ключевое слово в вакансии
            'payment_from': 0,  # Минимальна зарплата
            'published': 1,
            'page': 0,
            'count': 100
        }

    def __parse(self, vocations: list):
        data = []
        for v in vocations:
            try:
                salary_from = v["payment_from"]
            except (KeyError, TypeError):
                salary_from = 0
            try:
                salary_to = v["payment_to"]
            except (KeyError, TypeError):
                salary_to = 0
            try:
                salary_currency = v["salary"]["currency"]
            except (KeyError, TypeError):
                salary_currency = "USD"
            try:
                salary_gross = v["salary"]["gross"]
            except (KeyError, TypeError):
                salary_gross = False

            data.append(Vacancy(
                **{
                    "platform": "SuperJob",
                    "city": v["town"]["title"],
                    "vacancy": v["profession"],
                    "link": v["link"],
                    "experience": v["experience"]["title"],
                    "salary": {"from": salary_from,
                               "to": salary_to,
                               "currency": salary_currency,
                               "gross": salary_gross},
                    "description": v["candidat"]
                }
            ))
        return data

    def get_vacancies(self) -> list[Vacancy]:
        vocation_data = []
        api_url = 'https://api.superjob.ru/2.0/vacancies/'
        headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': self.api,
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application / x-www-form-urlencoded'
        }

        for i in range(1):
            self.__params['page'] = i
            response = requests.get(api_url, params=self.__params, headers=headers)
            row_data = response.json()['objects']
            vocation_data.extend(row_data)

        return self.__parse(vocation_data)

    def __str__(self):
        return self.keyword

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.keyword}')"
