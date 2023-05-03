#!/usr/bin/env python3
"""async generator func"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[int, None, None]:
    """ the function would loop 10x and yeild a random value"""
    for i in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0,10))
