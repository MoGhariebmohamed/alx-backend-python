#!/usr/bin/env python3
"""
this is module a floor
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    method to input list of float retutn float
    """
    return lambda multi: multi * multiplier
