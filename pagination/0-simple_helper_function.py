#!/usr/bin/env python3

"""
    Index Range
"""


def index_range(page, page_size):

    """ Index Range """

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
