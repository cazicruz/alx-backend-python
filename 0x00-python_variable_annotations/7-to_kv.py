#!/usr/bin/env python3
"""function annotation"""
from typing import List, Union


def to_kv(k: str, v: Union[int. float]) -> Tuple:
    """ this function retuns a tuple and it takes 
    a string and a integer or float"""
    x = (k, v*v)
    return x
