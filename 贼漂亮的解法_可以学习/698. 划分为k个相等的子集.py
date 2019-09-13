import itertools
import collections
import math
import re
import sys
from typing import List
MAXINF = float('inf')
MININF = -float('inf')

def read_int_lst():
    return list(map(int, input().split()))

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        t = sum(nums)
        if t % k != 0:
            return False
        nums = sorted(nums, reverse=True)
        return self.dfs(nums, t // k, 0, k, 0)

    def dfs(self, nums, target, cur, k, used):
        # 这里同时出现了cur 和 k 来标识当前的状态.
        # cur 表示当前的累计值， k表示还剩余多少组
        if k == 0:
            if used == 2 ** len(nums) - 1:
                return True
            else:
                return False
        # 遍历所有
        for i in range(len(nums)):
            # 如果已经走过了
            if used & (1 << i):
                continue
            # 用新的变量来标识
            t = cur + nums[i]
            # 剪枝，因为如果我们可以从大到小的排序的话，我们就可以
            # 省略很多的值
            if t > target:
                break
            # 新变量
            new_used = used | (1 << i)
            # 用两个状态的指针
            if t == target and self.dfs(nums, target, 0, k-1, new_used):
                return True
            elif self.dfs(nums, target, t, k, new_used):
                return True
        return False


nums = [4, 5, 3, 2, 5, 5, 5, 1, 5, 5, 5, 5, 3, 5, 5, 2]
k = 13
print(Solution().canPartitionKSubsets(nums, k))