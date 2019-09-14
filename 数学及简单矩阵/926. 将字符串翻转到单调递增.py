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
    def minFlipsMonoIncr(self, S: str) -> int:
        P = [0]
        for x in S:
            P.append(P[-1] + int(x))
        return min([P[j] + len(S) - j - (P[-1] - P[j]) for j in range(len(P))])

S = "010110"
print(Solution().minFlipsMonoIncr(S))