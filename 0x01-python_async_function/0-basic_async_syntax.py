#!/usr/bin/env puthon3
"""practicing asynchronous coroutine"""
import random


async def wait_random(max_delay: int =10):
    """waits for a randome delay and returns the param"""
    await.sleep(random.uniform(0, max_delay))
    return max_delay
