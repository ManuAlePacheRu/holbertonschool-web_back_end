#!/usr/bin/env python3

"""
Module for providing a floor function.
"""

import math


def floor(n: float) -> int:
    """
    Return the largest integer less than or equal to the given float.

    Parameters:
    n (float): The number to floor.

    Returns:
    int: The largest integer less than or equal to n.
    """

    return math.floor(n)
