def test_lfu_cache(dummy_lfu_cache):
    # Test lfu_cache.
    # The following measures can be used to explain the sequence of the test.
    #   * cnt(x) is the use counter for key x
    #   * cache=[] shows the last used order for tiebreakers (leftmost element is  most recent)
    #
    lfu = dummy_lfu_cache           # dummy_lfu_cache is a LFU cache with a capacity of limit 2.
    lfu.put(1, 1)                   # cache=[1,_], cnt(1)=1
    lfu.put(2, 2)                   # cache=[2,1], cnt(2)=1, cnt(1)=1
    actual = lfu.get(1)             # return 1
    expected = 1                    # cache=[1,2], cnt(2)=1, cnt(1)=2
    assert actual == expected, f"lfu.get(1) should return {expected}"

    lfu.put(3, 3)                   # 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                                    # cache=[3,1], cnt(3)=1, cnt(1)=2
    actual = lfu.get(2)             # return -1 (not found)
    expected = -1
    assert actual == expected, f"lfu.get(2) should return {expected}"

    actual = lfu.get(3)             # return 3
    expected = 3                    # cache=[3,1], cnt(3)=2, cnt(1)=2
    assert actual == expected, f"lfu.get(3) should return {expected}"

    lfu.put(4, 4)                   # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                                    # cache=[4,3], cnt(4)=1, cnt(3)=2
    actual = lfu.get(1)             # return -1 (not found)
    expected = -1
    # expected = 1
    assert actual == expected, f"lfu.get(1) should return {expected}"

    actual = lfu.get(3)             # return 3
    expected = 3                    # cache=[3,4], cnt(4)=1, cnt(3)=3
    assert actual == expected, f"lfu.get(3) should return {expected}"

    actual = lfu.get(4)             # return 4
    expected = 4                    # cache=[4,3], cnt(4)=2, cnt(3)=3
    assert actual == expected, f"lfu.get(4) should return {expected}"