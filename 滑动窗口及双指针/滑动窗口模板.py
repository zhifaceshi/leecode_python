import itertools
import collections
import math
import re
import sys
from typing import List

MAXINF = float('inf')
MININF = -float('inf')


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        count = MAXINF
        ans = None
        for i in range(len(nums)-2):
            t = target - nums[i]
            value = self.sliding_window(nums[i+1:], t)
            if value is not None:
                if count > abs(target - nums[i] - value):
                    count = abs(target - nums[i] - value)
                    ans = nums[i] + value
        return ans
    def sliding_window(self, nums, target):
        i = 0
        j = len(nums) -1
        ret = MAXINF
        ans = None
        while i < j:
            if ret > abs(nums[i] + nums[j] - target):
                ret = abs(nums[i] + nums[j] - target)
                ans = nums[i] + nums[j]
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                return target

        if ans is not None:
            return ans
        return None

nums = [0,0,0]
target = 1
print(Solution().threeSumClosest(nums, target))