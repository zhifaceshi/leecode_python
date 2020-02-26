#
# @lc app=leetcode.cn id=926 lang=python3
#
# [926] 将字符串翻转到单调递增
#

# @lc code=start
def get_count(s, char):
    num = 0
    for c in s:
        if c == char:
            num += 1
    return num

class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        prefix = [0] # 
        count = 0
        for c in S:
            if c == '1':
                count += 1
            prefix.append(count)


        return min([ prefix[i] + len(S) - i - prefix[-1] + prefix[i] for i in range(len(prefix)) ])



# @lc code=end
if __name__ == "__main__":
    print(Solution().minFlipsMonoIncr("00011000"))
