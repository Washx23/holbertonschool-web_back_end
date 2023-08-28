#!/usr/bin/env python3
"""module"""


from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of floating-point numbers in a list.

    Args:
        input_list (List[float]): The list of floating-point numbers.

    Returns:
        float: The sum of the numbers in the input list.
    """
    return sum(input_list)
