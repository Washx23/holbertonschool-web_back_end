#!/usr/bin/env python3
"""doc"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """module document"""
    delay_list = []
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        delay_list.append(delay)

    delay_list.sort()
    return delay_list
