#!/usr/bin/env python3
"""module"""


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Returns a list of tuples containing elements and their lengths.

    Args:
        lst (List[str]): The list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple contains a string and its length.
    """
    return [(i, len(i)) for i in lst]
