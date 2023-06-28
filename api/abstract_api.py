from abc import ABC, abstractmethod


class AbstractAPI(ABC):

    @abstractmethod
    def __init__(self, key_word: str):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass
