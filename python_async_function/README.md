#!/usr/bin/env python3

"""
    wait function
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """wait random function""

    time = random.uniform(0.0, float(max_delay))
    await asyncio.sleep(time)
    return time
