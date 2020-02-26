#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
from typing import *
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        candidates = list(range(1, n+1))
        if k >= len(candidates):
            return [candidates, ]
        ans = []
        self.dfs(candidates, [], k, ans)

        return ans

    def dfs(self, candidates, t, k, ans):
        if len(t) > k:
            return
        if len(t) == k:
            ans.append(list(t))
        else:
            for i in range(len(candidates)):
                self.dfs(candidates[i+1: ], t + [candidates[i],], k, ans)


# @lc code=end

if __name__ == "__main__":
    print(Solution().combine(4,2))