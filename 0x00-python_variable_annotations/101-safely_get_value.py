#!/usr/bin/env python3
"""annotation in python"""
from typing import Mapping, Any, Union, TypeVar


def safely_get_value(dct: Mapping, key: Any,default: Union[TypeVar('T'),
    None] = None) -> Union[Any, TypeVar('T')]:
    """returns the value of the dict key"""
    if key in dct:
        return dct[key]
    else:
        return default
