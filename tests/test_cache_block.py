def test_lfu_cache_store_length(dummy_cache_block):
    cb = dummy_cache_block
    assert 5 == cb.length()     # dummy_cache_block has a size of 5.


def test_lfu_cache_store_pop_left(dummy_cache_block):
    cb = dummy_cache_block
    assert 1 == cb.pop_left()
    assert 2 == cb.pop_left()
    assert 3 == cb.pop_left()


def test_lfu_cache_store_update(dummy_cache_block):
    cb = dummy_cache_block
    cb.update(1)
    assert 1 != cb.pop_left()