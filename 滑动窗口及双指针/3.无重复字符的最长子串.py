#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
# from collections import OrderedDict
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         maxvalue = 0
#         start = 0
#         dct = {}
        
#         for i, c in enumerate(s):
#             if c not in dct: # 这行代码的问题在于，会出现start > dct[c]的情况，这样会导致
#                 dct[c] = i
#             else:
#                 start = dct[c] + 1
#                 dct[c] = i
#             maxvalue = max(maxvalue, i + 1 - start)
#         return maxvalue

from collections import OrderedDict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxvalue = 0
        start = 0
        dct = {}
        
        for i, c in enumerate(s):
            if c not in dct:
                dct[c] = i
            else:
                start = dct[c] + 1 if start <= dct[c] else start
                dct[c] = i
            maxvalue = max(maxvalue, i + 1 - start)
        return maxvalue

# @lc code=end
if __name__ == "__main__":
    s = "abba" #
    print(Solution().lengthOfLongestSubstring(s))
