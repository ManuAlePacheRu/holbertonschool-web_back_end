#!/usr/bin/env python3

"""
Этот скрипт содержит функцию `element_length`,
которая принимает список последовательностей
и возвращает список кортежей,
где каждый кортеж состоит из последовательности и её длины.
"""

import typing


def element_length(
    lst: typing.Iterable[typing.Sequence]
) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    Принимает список последовательностей
    и возвращает список кортежей,
    где каждый кортеж содержит
    последовательность и её длину.

    :param lst: Список последовательностей (например, строк или списков).
    :type lst: typing.Iterable[typing.Sequence]
    :return: Список кортежей, каждый из которых
    содержит последовательность из `lst` и её длину.
    :rtype: typing.List[typing.Tuple[typing.Sequence, int]]
    """
    return [(i, len(i)) for i in lst]
