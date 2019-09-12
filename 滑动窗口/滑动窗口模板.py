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

def build_sliding_window(s):
    dct = collections.defaultdict(int)
    winsize = 10
    for i in range(len(s) - winsize + 1):
        j = i + winsize
        dct[s[i:j]] += 1
    return dct
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dct = build_sliding_window(s)
        ans = []
        for key, value in dct.items():
            if value > 1:
                ans.append(key)
        return ans

print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))