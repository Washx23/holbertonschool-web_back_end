#!/usr/bin/env python3
"""module"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing elements and their lengths.

    Args:
        lst (Iterable[Sequence]): The iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where
        each tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
