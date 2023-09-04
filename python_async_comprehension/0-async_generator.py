#!/usr/bin/env python3
"""documentation for task 0"""


import asyncio
import random


async def async_generator():
    """
    An asynchronous generator that yields random numbers between 0 and 10
    after waiting for 1 second in each iteration.

    Yields:
        int: A random integer between 0 and 10.

    Example:
        async def main():
            async for num in async_generator():
                print(num)

        if __name__ == "__main__":
            asyncio.run(main())
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Wait asynchronously for 1 second
        yield random.randint(0, 10)

# Example usage:
async def main():
    """mudule documentation"""
    async for num in async_generator():
        print(num)

if __name__ == "__main__":
    asyncio.run(main())
