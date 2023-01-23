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


if __name__ == "__main__":
    doctest.testmod()
    pass
