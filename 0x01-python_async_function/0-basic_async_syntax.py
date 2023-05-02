#!/usr/bin/env puthon3
"""practicing asynchronous coroutine"""
import random
import asyncio


async def wait_random(max_delay: int =10):
    """waits for a randome delay and returns the param"""
    await asyncio.sleep(random.uniform(0, max_delay))
    return max_delay

asyncio.run(wait_random())
