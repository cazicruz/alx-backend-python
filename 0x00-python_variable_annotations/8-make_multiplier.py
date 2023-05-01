#!/usr/bin/env python3
""" function annotation with callable"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a value and returns a function (mul) that takes another value
    and returns the multiplication of both values"""
    def mul(num: float) -> float:
        return(num * multiplier)
    return (mul)
