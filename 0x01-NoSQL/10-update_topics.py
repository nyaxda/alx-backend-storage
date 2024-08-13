#!/usr/bin/env python3
"""module for mongodb"""


def update_topics(mongo_collection, name, topics):
    """function that updates a document in a collection based on name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
