"""
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента
  функцию, которая принимает объект (любого типа) в качестве аргумента.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации
 о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).
"""

import inspect


def introspection_info(obj):
    info = {}

    info['Type'] = type(obj)
    info['Attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    info['Methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    info['Module'] = inspect.getmodule(obj)

    return info

    # Проверочный код:


number_info = introspection_info(42)
print(number_info)
