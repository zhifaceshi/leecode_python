import itertools
import collections
import math
import re
import sys
from typing import List
import functools

MAXINF = float('inf')
MININF = -float('inf')


from typing import *
import bisect


def g(l,r,mid,nums,target):
    # 无序
    if nums[l] > nums[r]:
        midvalue = nums[mid]
        if midvalue == target:
            return True
        left = nums[l]
        right = nums[r]
        if right < left <= midvalue:
            if left<=target<= midvalue:
                return True
        if midvalue <= right < left:
            if target > midvalue and target >= left:
                return True
            if target < midvalue:
                return True
    else:
        if nums[mid] >= target:
            return True
    return False

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if g(l,r,mid,nums,target):
                r = mid
            else:
                l = mid + 1
        return l

# nums = [3,1]
# target = 1
# nums = [4,5,6,7,0,1,2]
# nums = [5,1,3]
nums = [5,1,2,3,4]
for t in nums:
    print(Solution().search(nums, t))

# nums = [5,1,3]
# target = 3
# nums = [5,1,2,3,4]
# target = 1
# print(Solution().search(nums, target))