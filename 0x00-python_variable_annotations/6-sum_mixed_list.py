#!/usr/bin/env python3
"""function annotation"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ this function retuns the sum of the list"""
    return float(sum(mxd_list))
