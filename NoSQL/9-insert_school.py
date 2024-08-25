#!/usr/bin/env python3

"""
    Insert: Task 9
"""


def insert_school(mongo_collection, **kwargs):
    """ Insert: Task 9"""

    return mongo_collection.insert_one(kwargs).inserted_id
