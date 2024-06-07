#!/usr/bin/env python3
"""
this is module a floor
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    method to input list of float retutn float
    """
    return (k, float(v ** 2))
