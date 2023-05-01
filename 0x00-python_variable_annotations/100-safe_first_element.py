#!/usr/bin/env python3
"""Duck type annotation in python3"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, Nonetype]:
    """Returns the first element in lst"""
    if lst:
        return lst[0]
    else:
        return None
