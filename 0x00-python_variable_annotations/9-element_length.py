#!/usr/bin/env python3
""" Python annotations"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """the function takes an iterable (tuple, dic, list) and returns a list
    containing a tuple with a sequence and an integer"""
    return [(i, len(i)) for i in lst]
