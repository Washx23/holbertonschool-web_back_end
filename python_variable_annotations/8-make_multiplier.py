#!/usr/bin/env python3
"""module"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that
        takes a float argument and returns the product.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
