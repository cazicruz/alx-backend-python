#!/usr/bin/env python3
"""wait_n is a coroutines function that creates a list of delays"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int , max_delay: int) -> List[float]:
    """waits for wait_random function to execute n
    times and return a list of its return value"""
    task = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return[await task for task in task]
