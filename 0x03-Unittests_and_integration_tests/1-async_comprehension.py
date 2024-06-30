#!/usr/bin/env python3
"""
this is module excersise on coroutine
"""

import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        method to generate random nuber
        random() to generate random float
    """
    return [new_result async for new_result in async_generator()]
