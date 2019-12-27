# -*- coding:utf-8 -*-

class Solution():
    m = {}
    def cutRope(self, number):
        # write code here
        if number == 1:return 1
        if number == 2:return 1
        if number == 3:return 2
        if number in Solution.m:
            return Solution.m[number]
        value = []
        for i in range(1, number + 1):
            t = i * self.search(number - i)
            value.append(t)
        return max(value)

    def search(self, n):
        if n <= 1:
            return 1
        if n in Solution.m:
            return Solution.m[n]
        value = []
        for i in range(1, n+1):
            t = i * self.search(n - i)
            value.append(t)
        Solution.m[n] = max(value)
        return Solution.m[n]

import bisect


if __name__ == '__main__':
    # print(Solution().hasPath("ABCESFCSADEE",3,4,"ABCB"))
    print(Solution().cutRope(4))
    from functools import lru_cache

# # ABCB
# """
# ABC
# ESF
# CSA
# DEE
# """