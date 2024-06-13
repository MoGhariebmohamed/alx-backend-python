#!/usr/bin/env python3
"""
this is module excersise on coroutine
"""

import asyncio
import random
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
        method to generate random nuber
        random() to generate random float
    """
    return [new_result async for new_result in async_generator()]
