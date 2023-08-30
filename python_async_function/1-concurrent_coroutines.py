#!/usr/bin/env python3
"""module"""


import asyncio
import random
import heapq
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a
    random delay between 0
    and max_delay (inclusive) seconds.
    Returns the waited delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Asynchronous routine that spawns wait_random
    n times with specified max_delay.
    Returns a list of all
    the delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    heapq.heapify(delays)
    sorted_delays = [heapq.heappop(delays) for _ in range(len(delays))]

    return sorted_delays


async def main():
    n = 5
    max_delay = 10
    delays = await wait_n(n, max_delay)
    print("Delays:", delays)


if __name__ == "__main__":
    asyncio.run(main())
