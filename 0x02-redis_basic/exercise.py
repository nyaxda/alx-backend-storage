#!/usr/bin/env python3
""" module for redis"""

import redis
import uuid
from typing import Union, Optional, Callable, Any


class Cache:
    """Class for implementing a Cache"""

    def __init__(self) -> None:
        """Constructor"""
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Hashing method to store data in Redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str, fn: Optional[Callable] = None) -> Any:
        """Get Method from redis"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Coverts bytes to str"""
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Get an int from redis"""
        return self.get(key, fn=int)
