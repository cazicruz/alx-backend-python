#!/usr/bin/env python3
"""a function that returns an asyncio.task"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """creates a task object and returns it """
    task = asyncio.create_task(wait_random(max_delay))
    return task
