#!/usr/bin/env python3
"""module for mongodb"""


def schools_by_topic(mongo_collection, topic):
    """function that returns the list of school having a specific topic"""
    count = mongo_collection.find({"topics": topic})
    return count
