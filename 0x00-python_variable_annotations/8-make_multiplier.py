#!/usr/bin/env python3
""" function annotation with callable"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable:
    def mul(num: float) -> float:
        return(num * multiplier)
    return (mul)
