#!/usr/bin/env python3
"""
this is module excersise on coroutine
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
        method to generate random nuber
        random() to generate random float
    """
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
