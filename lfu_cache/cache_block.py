"""Doubly Linked Lists with LRU Evict Policy 

The doubly linked lists(DLL) maintain elements with the same use counter in order of use.
The most recently used(MRU) element will be pushed at the right. The least recently used(LRU) element will be popped from the left. 
The DLL allows us to access or remove elements at the right or left in O(1) time. 
On top of that, with the help of a cache map, we can access or remove any node in the list in O(1) time.
"""

import logging
from typing import Collection, Dict, List, Optional, Set, Tuple, Union


__all__ = [
    "LinkedList",
]

logger = logging.getLogger(__name__)

class Node:
    def __init__(self, key=-float("inf"), prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next


class LinkedList:
    """Doubly Linked Lists.
    Maintains elements that have the same use counter in order of use.
    The most recently used(MRU) element will be pushed at the right. The least recently used(LRU) element will be popped from the left. 
    This class has a cache map as a member variable, which allows us to access or remove any node in the list in O(1) time.
    """

    def __init__(self):
        """Initialize the object with the left and right senetinel nodes. 
        """
        self.left = Node()  #  Sentinel Node
        self.right = Node()  # Sentinel Node
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}     # Map key to node.


    def length(self):
        """"Get the size of cache."""
        return len(self.cache)


    def push_right(self, key):
        """Push a node at the right as it is most recently used (MRU)."""
        node = Node(key)
        node.prev = self.right.prev
        node.next = self.right
        self.cache[key] = node
        self.right.prev = node
        node.prev.next = node


    def pop(self, key):
        """Remove a node from anywhere in the list. It operates in O(1) time, with the help of the cache map."""
        if key in self.cache:
            node = self.cache[key]
            pred = node.prev
            succ = node.next

            pred.next = succ
            succ.prev = pred
            self.cache.pop(key, None)


    def pop_left(self):
        """Remove a node from the left as it is least recently used (LRU)."""
        result = self.left.next.key
        logger.info(f'result = {result}')
        self.pop(result)
        return result

    
    def update(self, key):
        """Place any cached node at the right. It operates in O(1) time."""
        self.pop(key)
        self.push_right(key)