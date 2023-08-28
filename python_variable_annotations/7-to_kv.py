#!/usr/bin/env python3
"""module"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string k as the first element
    and the square of the int/float v as the second element.

    Args:
        k (str): The string key.
        v (Union[int, float]): The int or float value.

    Returns:
        Tuple[str, float]: A tuple containing the key
        and the square of the value.
    """
    return k, v ** 2.0
