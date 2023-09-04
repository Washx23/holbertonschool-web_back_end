#!/usr/bin/env python3
"""documentation for task 4"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """module document Everything is documented"""
    delay_list = []
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        delay_list.append(delay)

    return sorted(delay_list)
