# Итератор для удаления дубликатов

class Unique(object):
    def __init__(self, items, ignore_case=False, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен
        # принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться
        # одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки,
        #           дна из них удалится
        # По-умолчанию ignore_case = False
        self.__list = iter(items)
        self.__unique_list = []
        self.__ignore_case = ignore_case
        pass


    def __next__(self):
        # Нужно реализовать __next__
       while True:
            el = self.__list.__next__()
            comp_el = None

            if self.__ignore_case and type(el) is str:
                comp_el = el.lower()
            else:
                comp_el = el

            if comp_el not in self.__unique_list:
                self.__unique_list.append(comp_el)
                return el

    def __iter__(self):
        return self

