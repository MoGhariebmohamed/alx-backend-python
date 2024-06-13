#!/usr/bin/env python3
"""
this is module excersise on coroutine
"""

import asyncio
import random
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        method to measure run time fo 4
    """
    initiating = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for any in range(4)))
    ending = time.perf_counter()
    return (ending - initiating)
async def main():
    return await(measure_runtime())

print(asyncio.run(main()))
