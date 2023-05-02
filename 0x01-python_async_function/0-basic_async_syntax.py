#!/usr/bin/env python3
"""practicing asynchronous coroutine"""
import random
import asyncio


async def wait_random(max_delay: int =10):
    """waits for a randome delay and returns the param"""
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
