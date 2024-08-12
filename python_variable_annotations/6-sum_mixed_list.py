#!/usr/bin/env python3
import typing

"""
    Sum the values of a list of int and float 
"""

def sum_mixed_list(mxd_list: typing.List[typing.Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing integers and floating-point numbers.

    Parameters:
    mxd_list (typing.List[typing.Union[int, float]]): A list of integers and/or floating-point numbers.

    Returns:
    float: The sum of the numbers in the list, represented as a float.
    """

    return sum(mxd_list)
