#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        else:
            ret= ["" for _ in range(numRows)]
            i = 0
            flag = -1
            for c in s:
                if i == 0 or i == numRows - 1:
                    flag *= -1
                ret[i] += c
                i += flag
        return "".join(ret)
        

# @lc code=end
if __name__ == "__main__":
    print(Solution().convert('LEETCODEISHIRING', 3))
