#!/usr/bin/env python3

""" 
    Schools by Topic: Task 11
"""


def schools_by_topic(mongo_collection, topic):
    """ Schools by Topic: Task 11"""

    return [doc for doc in mongo_collection.find()
            if (topics := doc.get('topics')) and topic in topics]
