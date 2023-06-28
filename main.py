from api.headhunter_api import HeadHunter
from api.superjob_api import SuperJob


def main():
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunter('Python')
    sj_api = SuperJob('Python')

    # Получение вакансий с разных платформ
    hh_vacancies = hh_api.get_vacancies()
    sj_vacancies = sj_api.get_vacancies()


def user_interaction():
    pass
