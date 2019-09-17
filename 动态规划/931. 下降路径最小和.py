import functools
MAXINF = float('inf')
MININF = -float('inf')
class Solution:
    grid = None
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        Solution.grid = A
        ans = []
        for j in range(len(A[0])):
            ans.append(self.dfs(len(A)-1, j))
        return min(ans)
    @functools.lru_cache(maxsize=None)
    def dfs(self, x, y):
        if x < 0:
            return 0
        if x < 0 or y < 0 or x >= len(Solution.grid) or y >= len(Solution.grid[0]):
            return MAXINF
        return min(self.dfs(x-1, y-1), self.dfs(x-1, y), self.dfs(x-1, y+1)) + Solution.grid[x][y]