from api.abstract_api import AbstractAPI

import os
import requests
import ujson


class HeadHunter(AbstractAPI):
    """ Класс для получения вакансий от ХХ по АПИ. """
    def __init__(self, keyword: str) -> None:
        self.keyword = keyword
        self.__params = {
            'text': 'NAME' + self.keyword,  # Поиск вакансии по передаваемой строке
            'area': 113,  # Поиск осуществляется по вакансиям города Москва
            'page': 0,  # Индекс страницы с вакансиями на ХХ
            'per_page': 100  # Количество вакансий на 1 странице
        }

    def get_vacancies(self) -> dict:
        """
        Метод для получения данных по заданной вакансии
        :return: список вакансий в формате json
        """
        hh_req = requests.get('https://api.hh.ru/vacancies', params=self.__params)
        hh_row_data = hh_req.content.decode()
        hh_req.close()
        hh_json = ujson.loads(hh_row_data)

        return hh_json

    def __str__(self):
        return self.keyword

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.keyword}')"


hh = HeadHunter('Python')
print(hh.get_vacancies())
