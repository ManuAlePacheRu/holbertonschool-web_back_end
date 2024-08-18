#!/usr/bin/env python3

'''
    basic async
'''

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ basic async """

    time = random.uniform(0.0, float(max_delay))
    await asyncio.sleep(time)
    return time
