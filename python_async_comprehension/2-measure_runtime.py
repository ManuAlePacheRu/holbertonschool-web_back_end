#!/usr/bin/env python3

"""
    measure runtime
"""

import asyncio
import time

async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure runtime """
    start_time = time.time()

    tasks = [async_comp() for i in range(4)]

    await asyncio.gather(*tasks)

    end_time = time.time()

    return end_time - start_time
