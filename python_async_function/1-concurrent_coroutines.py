#!/usr/bin/env python3
"""module"""


import asyncio
import random


async def wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n, max_delay=10):
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    delays.sort()
    return delays


async def main():
    n = 5
    max_delay = 10
    delays = await wait_n(n, max_delay)
    print("Delays:", delays)


if __name__ == "__main__":
    asyncio.run(main())
