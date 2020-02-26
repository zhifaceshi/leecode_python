#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] 和可被 K 整除的子数组
#

# @lc code=start
from typing import *
# class Solution:
#     A = []
#     count = 0
#     K = None
#     def subarraysDivByK(self, A: List[int], K: int) -> int:
#         dct = {}
#         count = 0
#         for winsize in range(1, len(A) + 1):
#             for i in range(len(A) - winsize + 1):
#                 j = i + winsize
#                 if (i+1, j) in dct:
#                     num = dct[(i+1, j)] + A[i]
#                 elif (i, j-1) in dct:
#                     num = dct[(i, j-1)] + A[j-1]
#                 elif (i+1, j-1) in dct:
#                     num = dct[(i+1, j-1)] + A[i] + A[j-1]
#                 else:
#                     num = sum(A[i:j])
#                     dct[(i, j)] = num
#                 if num % K == 0:
#                     count += 1
#         return count
# 又是一道前缀和的问题
from collections import Counter
import math
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        P = [0]
        for a in A:
            P.append(P[-1] + a)
        for i in range(len(P)):
            P[i] %= K
        c = Counter(P)
        count = 0
        for k, v in c.items():
            count += (v * (v-1)) // 2
        return count
            

# @lc code=end
if __name__ == "__main__":
    A = [4,5,0,-2,-3,1]
    K = 5
    print(Solution().subarraysDivByK(A, K))
