#!/usr/bin/env python3

"""
    All: Task8
"""


def list_all(mongo_collection):
    """ All: Task 8 """

    return [doc for doc in mongo_collection.find()]
