#!/usr/bin/env python3
"""function index_range that takes two integer arguments page and page_size"""
from typing import Tuple
import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Simple Pagination"""
        assert type(page) == int
        assert page > 0
        assert type(page_size) == int
        assert page_size > 0
        start, end = index_range(page, page_size)
        if start >= len(self.dataset()):
            return []
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Implementing hypermedia pagination"""
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {"page_size": page_size,
                "page": page,
                "data": self.get_page(page, page_size),
                "next_page": page + 1 if page + 1 <= total_pages else None,
                "prev_page": page - 1 if page > 1 else None,
                "total_pages": total_pages
                }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns the tuple"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
