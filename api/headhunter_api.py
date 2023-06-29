from api.abstract_api import AbstractAPI
from vacancy.vacancy import Vacancy
import requests


class HeadHunter(AbstractAPI):
    """ Класс для получения вакансий от ХХ по АПИ. """
    def __init__(self, keyword: str) -> None:
        self.keyword = keyword
        self.__params = {
            'text': 'NAME:' + self.keyword,  # Поиск вакансии по передаваемой строке
            'area': 113,  # Поиск осуществляется по вакансиям города Москва
            'page': 0,  # Индекс страницы с вакансиями на ХХ
            'per_page': 100  # Количество вакансий на 1 странице
        }

    def __parse(self, vocations: list):
        """Обрабатывает вакансии"""
        data = []
        for v in vocations:
            try:
                salary_from = v["salary"]["salary_from"]
            except (KeyError, TypeError):
                salary_from = 0
            try:
                salary_to = v["salary"]["salary_to"]
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
                    "platform": "HeadHunter",
                    "city": v["area"]["name"],
                    "vacancy": v["name"],
                    "link": v["alternate_url"],
                    "experience": v["experience"]["name"],
                    "salary": {"from": salary_from,
                               "to": salary_to,
                               "currency": salary_currency,
                               "gross": salary_gross},
                    "description": v["snippet"]["responsibility"]
                }
            ))
        return data

    def get_vacancies(self) -> list[Vacancy]:
        """
        Метод для получения данных по заданной вакансии
        :return: список экземпляров класса Vacancy
        """
        vocation_data = []
        for i in range(1):
            self.__params['page'] = i
            response = requests.get('https://api.hh.ru/vacancies', params=self.__params)
            row_data = response.json()['items']  # json method requests
            vocation_data.extend(row_data)

        return self.__parse(vocation_data)

    def __str__(self):
        return self.keyword

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.keyword}')"
