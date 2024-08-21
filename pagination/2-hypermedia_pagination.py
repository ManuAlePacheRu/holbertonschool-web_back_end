#!/usr/bin/env python3

"""
    Simple Pagination
"""

import csv
import math
from typing import List


def index_range(page, page_size):

    """ Index Range """

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Get Page """
        assert isinstance(page, int) and page >= 0
        assert isinstance(page_size, int) and page_size > 0
        x, z = index_range(page, page_size)
        dat = self.dataset()
        if len(dat) < z:
            return []
        ret_dat = dat[x:z]
        return ret_dat
    
    def get_hyper(self, page: int = 1, page_size: int = 10):

        """ Hypermedia Pagination """

        assert isinstance(page, int) and page >= 0
        assert isinstance(page_size, int) and page_size > 0
        dataset_length = len(self.dataset())
        pag_total = math.ceil(dataset_length / page_size)
        return {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if not page >= pag_total else None,
            'prev_page': page - 1 if not page <= 1 else None,
            'total_pages': pag_total
            }
