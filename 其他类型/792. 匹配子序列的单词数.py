import itertools
import collections
import math
import re
import sys
from typing import List
import functools

MAXINF = float('inf')
MININF = -float('inf')


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        words_dct = collections.Counter(words)
        count = 0
        for key, value in words_dct.items():
            if self.check(key, S):
                count += value
        return count
#https://leetcode-cn.com/problems/number-of-matching-subsequences/solution/python3jie-fa-by-wei-leng-_-2/
    def check(self, word, S):
        index = 0
        "".index()
        for i in range(len(word)):
            res = S.find(word[i], index)
            if -1 == res:
                return False
            else:
                index = res + 1
        return True

S = "abcde"
words = ["a", "bb", "acd", "ace"]
print(Solution().numMatchingSubseq(S, words))