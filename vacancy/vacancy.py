class Vacancy:

    def __init__(self, platform: str, city: str, vacancy: str, link: str, experience: str,
                 salary: dict, description: str) -> None:
        self.__platform = platform
        self.__city = city
        self.__vacancy = vacancy
        self.__link = link
        self.__experience = experience
        self.__salary = salary
        self.__description = description

        self.__salary_mid = (self.__conversion()["to"] - self.__conversion()["from"]) / 2

    def __conversion(self):
        salary_conv = self.__salary
        usd_rub = 80
        eur_rub = 85
        if self.__salary["currency"] == 'USD':
            salary_conv["from"] = self.__salary["from"] * usd_rub
            salary_conv["to"] = self.__salary["to"] * usd_rub
            salary_conv["currency"] = 'RUB'
        if self.__salary["currency"] == 'EUR':
            salary_conv["from"] = self.__salary["from"] * eur_rub
            salary_conv["to"] = self.__salary["to"] * eur_rub
            salary_conv["currency"] = 'RUB'
        return salary_conv

    def __gt__(self, other):
        """
         Этот метод сравнивает текущий объект с другим объектом,
         используя оператор "больше" (>). Он возвращает True,
         если текущий объект больше другого объекта, и
         False в противном случае.
        :param other:
        :return:
        """
        return self.__salary_mid > other.__salary_mid

    def __ge__(self, other):
        """
        Этот метод сравнивает текущий объект с другим объектом,
        используя оператор "больше или равно" (>=).
        Он возвращает True, если текущий объект больше или равен другому объекту,
        и False в противном случае.
        :param other:
        :return:
        """
        return self.__salary_mid >= other.__salary_mid

    def __lt__(self, other):
        """
        Этот метод сравнивает текущий объект с другим объектом,
        используя оператор "меньше" (<).
        Он возвращает True, если текущий объект меньше другого объекта,
        и False в противном случае.
        :param other:
        :return:
        """
        return self.__salary_mid < other.__salary_mid

    def __le__(self, other):
        """
         Этот метод сравнивает текущий объект с другим объектом,
         используя оператор "меньше или равно" (<=).
         Он возвращает True, если текущий объект меньше или равен другому объекту,
         и False в противном случае.
        :param other:
        :return:
        """
        return self.__salary_mid <= other.__salary_mid

    def __eq__(self, other):
        """
        Этот метод сравнивает текущий объект с другим объектом,
        используя оператор "равно" (==). Он возвращает True,
        если текущий объект равен другому объекту,
        и False в противном случае
        :param other:
        :return:
        """
        return self.__salary_mid == other.__salary_mid
