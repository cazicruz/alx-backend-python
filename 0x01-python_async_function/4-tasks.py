#!/usr/bin/env python3
"""re-creating wait_n"""
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int , max_delay: int) -> List[float]:
    """waits for task_wait_random function to execute n
    times and return a list of its return value"""
    task = [task_wait_random for _ in range(n)]
    return[await task for task in task]
