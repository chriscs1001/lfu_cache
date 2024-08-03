"""Least Frequently Used (LFU) Cache

The LFUCache class is designed to meet the following functional requirements:
    * Evict policy: remove the least frequently used(LFU) key when the cache is full. When there is a tie(keys at the same frequency), remove the least recently used(LRU) key.
    * Implement two public APIs, get and put:
        - get(self, key: int) -> int: return value or -1 if the key is not present.
        - put(self, key: int, value: int) -> None: insert the key-value pair object into the cache or update the value and the cache if the key exists.
    * The methods get and put must each run in O(1) average time complexity.

To determine the least frequently used key, a use counter is maintained for each key in the cache. 
The key with the smallest use counter is the least frequently used key.
When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). 
The use counter for a key in the cache is incremented either a get or put operation is called on it.

To make the get and put methods run in O(1) average time complexity, the doubly linked lists(DLLs) and hash maps are employed under the hood.
The DLLS maintains elements with the same use counter in order of use. The most recently used(MRU) element will be pushed at the right. 
The least recently used(LRU) element will be popped from the left. The DLL allows us to access or remove elements at the right or left in O(1) time. 
On top of that, with the help of a cache map, we can access or remove any node in the list in O(1) time.

For each element in the cache, we have hash maps to keep track of all keys and refer to nodes in the doubly linked lists. 
To access doubly linked lists at a specified use counter in constant time, a hash map (i.e., list_map) with count as keys and linked list as values has been used.
There are two other hash maps to use. The count_map is used to keep track of the number of times a key-value paired object is referenced in memory. 
The value_map maintains all the key-value paired objects in memory.

A min_count member variable is used to track the current minimum count for eviction.
"""

import logging
from typing import Collection, Dict, List, Optional, Set, Tuple, Union

from cache_block import LinkedList

__all__ = [
    "LFUCache",
]

logger = logging.getLogger(__name__)

logging.basicConfig(filename='lfu_cache.log', level=logging.ERROR)

from collections import defaultdict

class LFUCache:
    """Least Frequently Used (LFU) cache data structure.

    Keeps track of the number of times a key-value paired object is referenced in memory 
    and removes the object with the smallest use couter when the cache is full.
    If two or more objects with the same frequency, the least recently used key will be invalidated.
    The methods get and put each run in O(1) average time complexity.
    """

    def __init__(self, capacity: int):
        """Initialize the object with the capacity of the data structure."""
        self.capacity = capacity
        self.min_count = 0   # Keep track of the smallest use count.
        self.value_map = {}  # Map key to value
        self.count_map = defaultdict(int)  # Map key to count
        self.list_map = defaultdict(LinkedList)  # Map count of key to linkedlist
        

    def counter(self, key: int):
        """Maintain a use counter for each key in the cache to determine the least frequently used key.
        The key with the smallest use counter is the least frequently used key.
        """
        count = self.count_map[key]
        self.count_map[key] += 1
        self.list_map[count].pop(key)
        self.list_map[count+1].push_right(key)
        if count == self.min_count and self.list_map[count].length() == 0:
            self.min_count += 1


    def get(self, key: int) -> int:
        """Get the value of the key if the key exists in the cache. Otherwise, returns -1."""
        if key not in self.value_map:
            return -1
        self.counter(key)
        return self.value_map[key]


    def put(self, key: int, value: int) -> None:
        """Update the value of the key if present, or inserts the key if not already present.
        When the cache reaches its capacity, it should invalidate and remove the least frequently used key 
        before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), 
        the least recently used key would be invalidated.
        """
        if self.capacity == 0:
            return

        if key not in self.value_map and len(self.value_map) == self.capacity:
            result = self.list_map[self.min_count].pop_left()
            self.value_map.pop(result)
            self.count_map.pop(result)

        self.value_map[key] = value
        self.counter(key)
        self.min_count = min(self.min_count, self.count_map[key])
        logger.info(f'min_count = {self.min_count}')