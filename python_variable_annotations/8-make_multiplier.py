#!/usr/bin/env python3

"""
Этот скрипт содержит функцию `make_multiplier`,
которая создает функцию-умножитель.

Функция `make_multiplier` принимает один аргумент
`multiplier` типа `float`, который
представляет собой множитель. Она возвращает
функцию, которая принимает один аргумент `x` типа
`float` и возвращает результат умножения `x` на `multiplier`.

Пример использования:
    multiplier_func = make_multiplier(3.0)
    result = multiplier_func(4.0)  # Результат будет 12.0
"""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    Создает функцию, умножающую входное значение на заданный множитель.

    :param multiplier: Множитель, который будет
    использоваться для умножения.
    :type multiplier: float
    :return: Функция, которая принимает одно
    число и умножает его на `multiplier`.
    :rtype: typing.Callable[[float], float]
    """
    return lambda x: x * multiplier
