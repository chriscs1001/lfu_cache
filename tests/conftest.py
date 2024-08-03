from lfu_cache.cache_policy import LFUCache
from lfu_cache.cache_block import LinkedList
import pytest

@pytest.fixture(scope="session")
def dummy_cache_block():
    # Create a cache block of size 5
    cb = LinkedList()
    cb.push_right(1)
    cb.push_right(2)
    cb.push_right(3)
    cb.push_right(4)
    cb.push_right(5)
    return cb


@pytest.fixture(scope="session")
def dummy_lfu_cache():
    # Create a LFU cache with capacity of limit 2.
    lfu = LFUCache(2)
    return lfu


