#!/usr/bin/env python3
"""module for mongodb"""


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a collection based on kwargs"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
