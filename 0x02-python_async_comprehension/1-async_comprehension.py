#!/usr/bin/env python3
"""async generator func"""
from typing import Generator
import asyncio, random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[int, None, None]:
    """ returns 10 random value from async_generator"""
    return[await for i in async_generator()]
