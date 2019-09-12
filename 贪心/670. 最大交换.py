import itertools
import collections
import math
import re
import sys
from typing import *
MAXINF = float('inf')
MININF = -float('inf')

"""
最简单的贪心的思想是错的
输入：
98368
输出：
98368
预期：
98863
下一个排列的idea是错的
输入：
10909091
输出：
19909001
预期：
90909011
"""
# 最后题解还是贪心，只是要记录最后出现的数字的索引
# 然后从左到右扫描数字，如果之后存在更大的数字
import functools
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(map(int, list(str(num))))
        dct = {}
        for index, n in enumerate(num):
            dct[n] = index
        t = list(num)
        for i, pre in enumerate(num):
            maxvalue = -1
            maxindex = None
            for value, index in dct.items():
                if pre >= value or i > index:
                    continue
                else:
                    if maxvalue < value:
                        maxvalue = value
                        maxindex = index
            if maxindex:
                t[i], t[maxindex] = t[maxindex], t[i]
                break

        return functools.reduce(lambda x,y:x*10 + y, t)

98368
115
print(Solution().maximumSwap(115))