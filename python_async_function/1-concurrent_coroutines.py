#!/usr/bin/env python3
"""module"""


import asyncio
from wait_random_module import wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        list[float]: List of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)


async def main():
    """doc"""
    delays = await wait_n(5, 10)
    print("Delays:", delays)


if __name__ == "__main__":
    asyncio.run(main())
