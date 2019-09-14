import itertools
import collections
import math
import re
import sys
from typing import List
import functools

MAXINF = float('inf')
MININF = -float('inf')


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = []
        for w in intervals:
            if len(ans) == 0:
                ans.append(w)
            else:
                pre_x, pre_y = ans[-1]
                cur_x, cur_y = w
                if pre_y < cur_x:
                    ans.append(w)
                else:
                    if cur_y >= pre_y:
                        ans[-1][1] = cur_y
                    else:
                        continue
        return ans

m = [[1,4],[2,3]]
print(Solution().merge(m))



