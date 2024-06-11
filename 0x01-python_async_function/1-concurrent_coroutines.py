#!/usr/bin/env python3
"""
this is module excersise on coroutine
"""
import asyncio
import random
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines.py').wait_n


async def measure_time(n: int, max_delay: int = 10) -> List[float]:
    """
        method to measures delay time n times delay max_delay to run
        Args:
        n: th tasks run
        max_delay: the delaying rnadom max
    """
    initiating = time.time
    asyncio.run(wait_n(n, max_delay))
    total time = time.time() - initiating
    return total_time / no

n = 5
max_delay = 9

print(measure_time(n, max_delay))