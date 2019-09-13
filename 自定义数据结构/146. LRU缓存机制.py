import itertools
import collections
import math
import re
import sys
from typing import List
import functools

MAXINF = float('inf')
MININF = -float('inf')

class node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
class LRUCache:
    def __init__(self, capacity: int):
        self.dct = {}  # key: [key, val]
        self.capacity = capacity
        # 双向
        self.bi_lianbiao = collections.deque(maxlen=capacity)# [ke, val]

    def get(self, key: int) -> int:
        if key not in self.dct:
            return -1
        else:
            # 更新链表
            self.put(key, self.dct[key].val)
            return self.dct[key].val

    def put(self, key: int, value: int) -> None:
        new_node = node(key, value)
        if key in self.dct:
            self.bi_lianbiao.remove(self.dct[key])
            self.bi_lianbiao.append(new_node)
            self.dct[key] = new_node
        else:
            if len(self.bi_lianbiao) == self.capacity:
                last = self.bi_lianbiao.popleft()
                del self.dct[last.key]
            self.bi_lianbiao.append(new_node)
            self.dct[key] = new_node


###python 更快的解法！！！！！！！！！！！！！！
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
    def get(self, key):
        if not key in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)
cache.put(1,1)
cache.put(2,2)
cache.get(1)
cache.put(3,3)
cache.get(2)
cache.put(4,4)
cache.get(1)
cache.get(3)
cache.get(4)