#!/usr/bin/env python3
"""
this is module excersise on coroutine
"""
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
        method to spawn n times delay max_delay to run
    """
    delay_time = [task_wait_random(max_delay) for _ in range(n)]
    actual_delays = await asyncio.gather(*delay_time)
    return sorted(actual_delays)
