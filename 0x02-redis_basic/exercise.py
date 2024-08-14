#!/usr/bin/env python3
""" module for redis"""

import redis
import uuid
from typing import Union


class Cache:
    """Class for implementing a Cache"""

    def __init__(self):
        """Constructor"""
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Hashing method to store data in Redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
