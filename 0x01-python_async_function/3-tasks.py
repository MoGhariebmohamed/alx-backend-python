#!/usr/bin/env python3
"""
this is module excersise on coroutine
"""
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
        method to measures delay time n times delay max_delay to run
        Args:
        n: th tasks run
        max_delay: the delaying rnadom max
    """

    return asyncio.create_task(wait_random(max_delay))
