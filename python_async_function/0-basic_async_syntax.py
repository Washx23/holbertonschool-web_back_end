#!/usr/bin/env python3
"""module"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay and returns it.

    Args:
        max_delay (int, optional):
        The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The random delay.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def main() -> None:
    random_delay: float = await wait_random()
    print(f"Random delay: {random_delay:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
