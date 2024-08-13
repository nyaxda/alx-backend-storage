#!/usr/bin/env python3
"""module for mongodb"""


def list_all(mongo_collection):
    return [doc for doc in mongo_collection.find()]
