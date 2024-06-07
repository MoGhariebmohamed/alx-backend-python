#!/usr/bin/env python3
"""
this is module a floor
"""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    method to input list of float retutn float
    """
    return [(i, len(i)) for i in lst]
