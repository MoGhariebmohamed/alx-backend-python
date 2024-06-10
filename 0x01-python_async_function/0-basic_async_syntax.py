#!/usr/bin/env python3
"""
this is module excersise on coroutine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        method to delay max_delay to run
    """
    delay_time = random.random() * max_delay
    await asyncio.sleep(delay_time)
    return delay_time
