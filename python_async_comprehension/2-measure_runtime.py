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
    tasks = []
    s_time = time.time()
    for i in range(4):
        asyncio.gather(async_comp())
    await asyncio.gather(*tasks)

    e_time = time.time()

    return s_time - e_time
