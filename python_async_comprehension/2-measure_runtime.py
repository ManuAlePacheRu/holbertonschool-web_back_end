#!/usr/bin/env python3

"""
    measure runtime
"""

import asyncio
import typing
import time

async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure runtime """
    s_time = time.time()

    tasks = [async_comp() for i in range(4)]

    await asyncio.gather(*tasks)

    e_time = time.time()

    return s_time - e_time
