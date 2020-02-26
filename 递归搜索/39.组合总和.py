#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from typing import *
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates, reverse=True)
        ans = []
        self.dfs(candidates, target, [], ans)
        return ans
    def dfs(self,candidates, target, t, ans):
        if target < 0:
            return
        if target == 0:
            a = sorted(list(t))
            if a not in ans:
                ans.append(a) 
            return 
        for v in candidates:
            self.dfs(candidates, target - v, t + [v, ], ans)


# @lc code=end

if __name__ == "__main__":
    a = Solution().combinationSum(candidates = [2,3,6,7], target = 7)
    print(a)