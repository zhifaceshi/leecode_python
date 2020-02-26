#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
from typing import *
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates, reverse=True)
        ans = []
        self.func(candidates, target, [], ans)
        return ans

    def func(self, candidates, target, t, ans):
        if target < 0:
            return 
        if target == 0:
            a = sorted((t))
            if a not in ans:
                ans.append(a)
        for i in range(len(candidates)):
            self.func( candidates[i+1:], target - candidates[i], t + [candidates[i], ], ans)

# @lc code=end

if __name__ == "__main__":
    print(Solution().combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))