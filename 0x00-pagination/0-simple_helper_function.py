#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes"""
    start_index = page_size * (page - 1)
    end_index = page * page_size
    return (start_index, end_index)