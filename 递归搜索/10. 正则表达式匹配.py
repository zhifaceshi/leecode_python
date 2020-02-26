"""
@Time    :2019/12/27 13:57
@Author  : 梁家熙
@Email:  :11849322@mail.sustech.edu.cn
"""
import json
from tqdm import tqdm
import random
from pprint import pprint
import os
import collections
from typing import List, Dict, Tuple
import logging

# 动态规划来求解答案
# class Solution(object):
#     def isMatch(self, text, pattern):
#         dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
#         # 设定末尾的空串是为真
#         dp[-1][-1] = True
#         for i in range(len(text), -1, -1):
#             for j in range(len(pattern) - 1, -1, -1):
#                 first_match = i < len(text) and pattern[j] in {text[i], '.'}
#                 if j+1 < len(pattern) and pattern[j+1] == '*':
#                     dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
#                 else:
#                     dp[i][j] = first_match and dp[i+1][j+1]
#
#         return dp[0][0]

# 考虑到状态转移
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0 and len(s) != 0:
            return False
        if len(p) == 0 and len(s) == 0:
            return True

        if p[-1] not in ['*', '.']:
            return self.isMatch(s[:-1], p[:-1])
        elif p[-1] == '*':
            if p[-2] == '.':
                return any([self.isMatch(s[:i], p[:-2]) for i in range(len(s) + 1)])
            else:
                return any([self.isMatch() ])
        elif p[-1] == '.':
            return self.isMatch(p[:-1], s[:-1])
        else:
            raise Exception


if __name__ == '__main__':

    s = "aa"
    p = "a"
    assert Solution().isMatch(s, p) == False

    s = "aa"
    p = "a*"
    assert Solution().isMatch(s, p) == True

    s = "ab"
    p = ".*"
    assert Solution().isMatch(s, p) == True

    s = "aab"
    p = "c*a*b"
    assert Solution().isMatch(s, p) == True

    s = "mississippi"
    p = "mis*is*p*."
    assert Solution().isMatch(s, p) == False