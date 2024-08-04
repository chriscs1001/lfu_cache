## lfu_cache

## Least Frequently Used (LFU) Cache

Least Frequently Used is a cache policy used to manage memory in a computer. It keeps track of the number of times
a block is referenced in memory and removes the element with the lowest reference frequency when the cache is full.

A data structure for a Least Frequently Used (LFU) cache is designed and implemented using Python.

The LFUCache class must meet the following functional requirements:

- Eviction policy: remove the least frequently used(LFU) key when the cache is full. When there is a tie(keys at the same frequency), remove the least recently used(LRU) key.
- Implement two public APIs, get and put:
  - get(self, key: int) -> int: return value or -1 if the key is not present.
  - put(self, key: int, value: int) -> None: insert the key-value pair object into the cache or update the value and the cache if the key exists.
- The methods get and put must each run in O(1) average time complexity.

To determine the least frequently used key, a use counter is maintained for each key in the cache.
The key with the smallest use counter is the least frequently used key.
When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation).
The use counter for a key in the cache is incremented either a get or put operation is called on it.

To meet the requirements to make the get and put methods run in O(1) average time complexity, the doubly linked lists(DLLs) and hash maps are employed under the hood.
The DLLs maintains elements with the same use counter in order of use. The most recently used(MRU) element will be pushed at the right.
The least recently used(LRU) element will be popped from the left. The DLL allows us to access or remove elements at the right or left in O(1) time.
On top of that, with the help of a cache map, we can access or remove any node in the list in O(1) time.

For each element in the cache, we have hash maps to keep track of all keys and refer to nodes in the doubly linked lists.
To access doubly linked lists at a specified use counter in constant time, a hash map (i.e., list_map) with count as keys and linked list as values has been used.
There are two other hash maps to use. The count_map is used to keep track of the number of times a key-value paired object is referenced in memory.
The value_map maintains all the key-value paired objects in memory.

A min_count member variable is used to track the current minimum count for eviction.

This Python implementation is an enhanced version of my solution that passed all the test cases of [Leetcode 460: LFU Cache](https://leetcode.com/problems/lfu-cache/description/).

Please feel to use it and enjoy it! Any contribution will be welcome. Please check out the contributing guidelines if you wish to make.

## Real World Applications of LFU Cache

Consider Redis servers. They typically sit between Application servers and Database servers when used as an in-memory cache.
Redis's Least Frequently Used (LFU) cache eviction mode removes the least accessed keys from the cache to make room for new data.
Redis keeps track of how often each key is accessed by incrementing a counter each time it's read or written. When the cache is full,
Redis evicts the keys with the lowest counter values to maintain a high hit rate for frequently accessed data.
[Redis's Cache Eviction](https://redis.io/docs/latest/develop/reference/eviction/)

LFU can be useful in situations where there's occasional access to many different keys, or when access patterns are consistent.
For example, search engines use LFU to invalidate query caches, removing the least frequently used queries first.
LFU can also help maintain a high hit rate for frequently accessed data, since those keys are more likely to remain in memory.
However, LFU might keep infrequently used data if it was accessed multiple times in the past.

## Installation

```bash
$ pip install lfu_cache
```

## Usage

```python
from cache_policy import LFUCache
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`lfu_cache` was created by Chris Chang Seong. It is licensed under the terms of the MIT license.
