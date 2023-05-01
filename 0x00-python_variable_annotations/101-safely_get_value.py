#!/usr/bin/env python3
"""annotation in python"""
from typing import Mapping, Any, Union


def safely_get_value(dct: Mapping, key: Any, default:Union[~T, None] = None) -> Union[Any, ~T]:
    """returns the value of the dict key"""
    if key in dct:
        return dct[key]
    else:
        return default
