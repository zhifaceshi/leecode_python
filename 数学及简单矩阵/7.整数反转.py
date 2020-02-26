#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        n = str(x)
        if x < 0:
            ans =  int(n[1: ][::-1]) * (-1) 
            if check(ans):
                return ans
            else:
                return 0
        else:
            ans =  int(n[::-1])
            if check(ans):
                return ans
            else:
                return 0
def check(x):
    if -2**31 <= x <= 2**31 - 1:
        return True
    return False
# @lc code=end


