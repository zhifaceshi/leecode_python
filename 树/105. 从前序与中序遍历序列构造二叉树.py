"""
@Time    :2019/12/26 14:06
@Author  : 梁家熙
@Email:  :11849322@mail.sustech.edu.cn
"""
import json
from tqdm import tqdm
import random
from pprint import pprint
import os
import collections
from typing import List, Dict, Tuple
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 and len(inorder) == 0:
            return None
        assert len(preorder) == len(inorder)

        root_val = preorder[0]
        index = inorder.index(root_val)


        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1: 1 + index], inorder[: index])
        root.right = self.buildTree(preorder[index + 1: ], inorder[index + 1: ])
        return root

if __name__ == '__main__':
    a = [1, 2]
    b = [2, 1]
    s = Solution().buildTree(a, b)


    def preorder(root):
        if root is None:
            return
        else:
            print(root.val, end='\t')
            preorder(root.left)
            preorder(root.right)
    preorder(s)