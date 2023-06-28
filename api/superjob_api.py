from api.abstract_api import AbstractAPI

import os
import requests
import ujson


class SuperJob(AbstractAPI):

    # api: str = os.environ.get("SUPERJOB_API")

    def __init__(self, keyword: str) -> None:
        self.keyword = keyword
        self.__params = {
            'keywords': [keyword],  # Ключевое слово в вакансии
            'payment_from': 0,  # Минимальна зарплата
            'published': 1
        }

    def get_vacancies(self):
        api_url = 'https://api.superjob.ru/2.0/vacancies/'
        headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': 'v3.r.137630020.d0ae84775cfab5b574e35b4464d652a3fc2b0ada.f737d25ba5f3a6c85fb84b5e16edb78e6cd9f545',
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application / x-www-form-urlencoded'
        }

        response = requests.get(api_url, params=self.__params, headers=headers)
        # sj_json = response.json()

        row_date = response.content.decode()
        sj_json = ujson.loads(row_date)

        return sj_json

    def __str__(self):
        return self.keyword

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.keyword}')"


sj = SuperJob('Python')
print(sj.get_vacancies())
