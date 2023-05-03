#!/usr/bin/env python3
""" function calculates the time of execution of wait_n"""
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ calculates the time of execution of wait_n
    with the  help of time.perf_counter
    which gives us the start time and end time"""
    s = time.perf_counter()
    wait_n(n, max_delay)
    execution_time = time.pref_counter() - s
    return execution_time
