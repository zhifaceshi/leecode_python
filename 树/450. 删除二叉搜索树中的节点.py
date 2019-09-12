import itertools
import collections
import math
import re
import sys
from typing import List

MAXINF = float('inf')
MININF = -float('inf')


def read_int_lst():
    return list(map(int, input().split()))


def build_3dmatrix(a, b, c, val=0):
    data = []
    for i in range(a):
        tt = []
        for j in range(b):
            t = []
            for k in range(c):
                t.append(val)
            tt.append(t)
        data.append(tt)
    return data


def build_2d_matrix(a, b, val=0):
    data = []
    for i in range(a):
        t = []
        for j in range(b):
            t.append(val)
        data.append(t)
    return data

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 参考如下图解
# https://leetcode-cn.com/problems/delete-node-in-a-bst/solution/yong-qian-qu-huo-zhe-hou-ji-jie-dian-zi-shu-dai-ti/
class Solution:
    flag = False
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        Solution.flag = False
    def find_pre(self, root):
        if root.right is None:
            return root
        return self.find_pre(root.right)
    def dfs(self, root, key):
        if Solution.flag:
            return root
        if root.val == key:
            if root.left is None:
                Solution.flag = True
                return root.right
            elif root.right is None:
                Solution.flag = True
                return root.left
            else:
                return self.find_pre(root.left)
        root.left = self.dfs(root.left, key)
        root.right = self.dfs(root.right, key)
        return root

