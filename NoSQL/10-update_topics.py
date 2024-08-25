#!/usr/bin/env python3

""" 
    Update Topics: Task 10
"""


def update_topics(mongo_collection, name, topics):
    """ Update Topics: Task 10"""

    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
