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
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_index = len(nums) - k
        l = 0
        r = len(nums)
        while l < r:
            mid = self.part(nums, l, r)
            if mid == target_index:
                return nums[mid]
            elif mid > target_index:
                r = mid
            else:
                l = mid + 1

    def part(self, nums, l, r):
        r -= 1
        base = nums[l]
        i = l

        while l < r:
            while l < r and nums[r] > base:
                r -= 1
            while l < r and nums[l] <= base:
                l += 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
        if l == r:
            nums[i], nums[l] = nums[l], nums[i]
        return l


arr =  [3,2,3,1,2,4,5,5,6]
k = 4

print(Solution().findKthLargest(arr, k))