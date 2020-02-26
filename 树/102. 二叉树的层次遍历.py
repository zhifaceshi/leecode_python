"""
@Time    :2019/12/27 15:18
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

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None: return []
        result = []
        queue = [root]
        while len(queue) != 0:
            length = len(queue)
            result.append([w.val for w in queue])
            while length != 0:
                length -= 1
                t = queue.pop(0)

                if t.left != None:
                    queue.append(t.left)
                if t.right != None:
                    queue.append(t.right)

        return result