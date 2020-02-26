
import lightgbm as lgb
lgb.LGBMClassifier
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val)

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        for i in range(len(matrix) // 2 + 1):
            for (n, m) in g(i, len(matrix) - i*2 ):
                print(matrix[n][m])

def g(i, s):
    x,y = i,i
    for a in range(s):
        yield x, y + a
    y += s -1
    for a in range(1, s):
        yield x + a, y
    x += s -1
    for a in range(1, s):
        yield x, y-a
    y -= s -1
    for a in range(1, s-1):
        yield x-a, y

if __name__ == '__main__':

    m = [
        [1,2,  3, 4],
        [5,6,  7, 8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    Solution().printMatrix(m)