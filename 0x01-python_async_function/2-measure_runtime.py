#!/usr/bin/env python3
"""
this is module excersise on coroutine
"""
import asyncio
import random
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        method to measures delay time n times delay max_delay to run
        Args:
        n: th tasks run
        max_delay: the delaying rnadom max
    """
    initiating = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - initiating
    return total_time / n
