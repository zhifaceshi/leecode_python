#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
import bisect
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            cur_v = nums[i]
            if cur_v in map:
                return [map[cur_v], i]
            else:
                map[target - cur_v] = i

# @lc code=end

if __name__ == "__main__":
    print(Solution().twoSum([2,7,11,15], 9))