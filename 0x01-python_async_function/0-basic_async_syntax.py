#!/usr/bin/env python3
"""practicing asynchronous coroutine"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """waits for a randome delay(rand) and returns the delay"""
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
