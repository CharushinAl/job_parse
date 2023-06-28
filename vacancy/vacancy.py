class Vacancy:

    def __init__(self, vacancy: str, link: str, salary: str, description: str) -> None:
        self.vacancy = vacancy
        self.link = link
        self.salary = salary
        self.description = description

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __le__(self, other):
        return self.salary <= other.salary
