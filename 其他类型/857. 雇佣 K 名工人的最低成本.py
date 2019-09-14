import itertools
import collections
import math
import re
import sys
from typing import List
import functools
import heapq

MAXINF = float('inf')
MININF = -float('inf')


# 先对工资比排序，小的放在前面。
# 堆里存放，到目前为止，k个最少工时的人


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        t = sorted([(w / q , q, w) for w , q in zip(wage, quality)])
        pool = []
        ans = MAXINF
        t_sum = 0
        for ratio, q, w in t:
            # 为什么是 -q，这不是大根堆嘛？
            "没错，为了维护k个最小值，要用大根堆才行。"
            heapq.heappush(pool, -q)
            t_sum += q
            if len(pool) > K:
                t_sum += heapq.heappop(pool)
            if len(pool) == K:
                ans = min(ans, ratio * t_sum)
        return ans

quality = [3,1,10,10,1]
wage = [4,8,2,2,7]
K = 3
print(Solution().mincostToHireWorkers(quality, wage, K))