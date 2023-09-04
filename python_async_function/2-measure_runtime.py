#!/usr/bin/env python3
""" Measure runtime for wait_n """

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """ Measure the time taken for wait_n to complete n times """
    start_time = time.time()
    
    # Run wait_n n times
    for _ in range(n):
        asyncio.run(wait_n(1, max_delay))
    
    end_time = time.time()
    
    # Calculate the average time taken per execution
    average_time = (end_time - start_time) / n if n > 0 else 0.0
    
    return average_time

if __name__ == "__main__":
    # Example usage:
    num_executions = 5
    max_delay = 10
    average_runtime = measure_time(num_executions, max_delay)
    print(f"Average runtime per execution: {average_runtime:.2f} seconds")
