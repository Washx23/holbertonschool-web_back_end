#!/usr/bin/env python3
"""module"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of integers and floats in a mixed list.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats.

    Returns:
        float: The sum of the numbers in the mixed list.
    """
    return sum(mxd_lst)
