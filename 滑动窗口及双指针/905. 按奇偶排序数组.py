import itertools
import collections
import math
import re
import sys
from typing import List
import functools

MAXINF = float('inf')
MININF = -float('inf')


def read_int_lst():
    return list(map(int, input().split()))


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A) - 1
        while i < j:
            while i < len(A) and A[i] % 2 == 0:
                i += 1
            while j > 0 and A[j] % 2 == 1:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
        return A
