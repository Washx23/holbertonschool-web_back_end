#!/usr/bin/env python3
"""module"""


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for 
    wait_n(n, max_delay) and return the average time per task.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: Average execution time per task.
    """
    start_time = time.time()

    await wait_n(n, max_delay)

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n


async def main():
    n = 5
    max_delay = 10

    average_time = await measure_time(n, max_delay)
    print(f"Average time per task: {average_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
