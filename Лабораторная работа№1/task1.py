import doctest


class Wood:
    def __int__(self, allowable_load: (int, float), current_load: (int, float)):
        """
        Создание и подготовка к работе объекта "Древесина"

        :param allowable_load: Допустимая нагрузка
        :param current_load: Текущая нагрузка

        Примеры:
        >>> wood = Wood(200, 81.5)
        """

        if not isinstance(allowable_load, (int, float)):
            raise TypeError('Допустимая нагрузка должна быть типом int или float')
        if not allowable_load > 0:
            raise ValueError('Допустимая нагрузка должна быть положительной')
        self.allowable_load = allowable_load

        if not isinstance(current_load, (int, float)):
            raise TypeError('Текущая нагрузка должна быть типом int или float')
        if current_load < 0:
            raise ValueError('Текущая нагрузка не может быть отрицательным числом')
        self.current_load = current_load

    def is_not_loaded(self) -> bool:
        """
        Функция проверяет нагружена ли древесина вообще

        :return: Нагружена ли древесина

        Примеры:
        >>> wood = Wood(200, 0)
        >>> wood.is_not_loaded()
        """
        ...

    def additioanl_loading(self, load: (int, float)) -> None:
        """
        Дополнительное нагружение древесины

        :param load: Какая нагрузка была дополнительно приложена
        :raise ValueError: Если сумма дополнительной и текущей нагрузки превышает допустимую, то вызыввем ошибку

        Примеры:
        >>> wood = Wood(200, 81.5)
        >>> wood.additioanl_loading(190)
        """
        if not isinstance(load, (int, float)):
            raise TypeError('Дополнительная нагрузка должна быть типом int или float')
        if load < 0:
            raise ValueError('Дополнительная нагрузка должна быть положительным числом')
        ...

        
 class VK:
    def __int__(self, allowed_number_of_users: int, current_number_of_users: int):
        """
        Создание и подготовка к работе объекта "VK"

        :param allowed_number_of_users: Допустимое колчиество пользователей на сайте
        :param current_number_of_users: Текущее колчиество пользователей на сайте

        Примеры:
        >>> vk = VK(1500, 500)
        """

        if not isinstance(allowed_number_of_users, int):
            raise TypeError('Допустимое колчиество пользователей должно быть типом int')
        if not allowed_number_of_users > 0:
            raise ValueError('Допустимое колчиество пользователей должно быть положительным')
        self.allowed_number_of_users = allowed_number_of_users

        if not isinstance(current_number_of_users, (int, float)):
            raise TypeError('Текущее колчиество пользователей должно быть типом int')
        if current_number_of_users < 0:
            raise ValueError('Текущее колчиество пользователей не может быть отрицательным числом')
        self.current_number_of_users = current_number_of_users

    def is_not_used(self) -> bool:
        """
        Функция проверяет пользуется ли сайтом хоть один человек

        :return: На сайте в данный момент времени никого нет из пользователей

        Примеры:
        >>> vk = VK(1500, 0)
        >>> vk.is_not_used()
        """
        ...

    def influx_of_users(self, users: int) -> None:
        """
        Количство новых пользователей

        :param users: Количество пользователей, зашедших на сайт
        :raise ValueError: Если колчисество новых и текущих пользователей превышает допустимое, то вызыввем ошибку

        Примеры:
        >>> vk = VK(1500, 500)
        >>> vk.influx_of_users(973)
        """
        if not isinstance(users, int):
            raise TypeError('Количество новых пользователей должно быть типом int')
        if users < 0:
            raise ValueError('Количество новых пользователей должно быть положительным числом')
        ...


class Table:
    def __int__(self, number_of_seats: int, number_of_occupied_places: int):
        """
        Создание и подготовка к работе объекта "Table"

        :param number_of_seats: Общее число мест за столом
        :param number_of_occupied_places: Число занятых мест за столом

        Примеры:
        >>> table = Table(20, 15)
        """

        if not isinstance(number_of_seats, int):
            raise TypeError('Общее число мест за столом должно быть типом int')
        if not number_of_seats > 0:
            raise ValueError('Общее число мест за столом должно быть положительным')
        self.number_of_seats = number_of_seats

        if not isinstance(number_of_occupied_places, (int, float)):
            raise TypeError('Число занятых мест за столом должно быть типом int')
        if number_of_occupied_places < 0:
            raise ValueError('Число занятых мест за столом не может быть отрицательным числом')
        self.number_of_occupied_places = number_of_occupied_places

    def is_not_occupied(self) -> bool:
        """
        Функция проверяет сидит ли за столом хоть один человек

        :return: Стол в данный момент времени никем не занят

        Примеры:
        >>> table = Table(20, 0)
        >>> table.is_not_occupied()
        """
        ...

    def new_occupied_seats(self, seats: int) -> None:
        """
        Число новых занятых мест

        :param seats: Число новых занятых мест
        :raise ValueError: Если сумма новых и ранее занятых мест превышает общее, то вызыввем ошибку

        Примеры:
        >>> table = Table(20, 15)
        >>> table.new_occupied_seats(4)
        """
        if not isinstance(seats, int):
            raise TypeError('Число новых занятых мест должно быть типом int')
        if seats < 0:
            raise ValueError('Число новых занятых мест должно быть положительным числом')
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
