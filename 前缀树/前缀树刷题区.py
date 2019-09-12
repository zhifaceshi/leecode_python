import itertools
import collections
import math
import re
import sys
from typing import List
MAXINF = float('inf')
MININF = -float('inf')

def read_int_lst():
    return list(map(int, input().split()))

class Trie():
    def __init__(self):
        self.root = {}

    def insert(self, word):
        p = self.root
        for w in word:
            if w not in p:
                p[w] = {}
            p = p[w]

        p['#'] = True

    def search(self, word):
        root = self.find(word)
        if root is not None and '#' in root:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) is not None

    def find(self, word):
        p = self.root
        for w in word:
            if w not in p:
                return None
            p = p[w]
        return p

class wordSub(Trie):

    def judge(self, word):
        t = self.root
        for i, c in enumerate(word):
            if '#' in t:
                return word[: i]
            elif c not in t:
                break
            t = t[c]
        return word


def convert(num):
    # print(convert(10))
    # 00000000000000000000000000001010
    num = bin(num)[2:].zfill(32)
    return num


class Solution:
    def __init__(self):
        self.root = {}

    def findMaximumXOR(self, nums: List[int]) -> int:
        for n in map(convert, nums):
            self.insert(n)
        count = 0
        for n in map(convert, nums):
            count = max(count, self.bianli(n))
        return count

    def insert(self, convert_num):
        p = self.root
        for w in convert_num:
            if w not in p:
                p[w] = {}
            p = p[w]
        p['#'] = True

    def bianli(self, query):
        p = self.root
        ans = 0
        for index, w  in enumerate(query):
            if w == '1' :
                new_w = '0'
            else:
                new_w = '1'
            if new_w in p:
                ans += 1 << (31 - index)
                p = p[new_w]
            else:
                p = p[w]
        return ans

print(Solution().findMaximumXOR([3, 10, 5, 25, 2, 8]))