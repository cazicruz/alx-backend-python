#!/usr/bin/env python3
"""time calculation code for an async func"""

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ returns the time it takes to execute async_comprehension 4x"""
    s = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
            async_comprehension(), async_comprehension())
    m = time.perf_counter() - s
    return m
