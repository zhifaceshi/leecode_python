import itertools
import collections
import math
import re
import sys
from typing import List
MAXINF = float('inf')
MININF = -float('inf')


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)
def preorder(root):
    if root is None:
        return
    else:
        print(root.val ,end='\t')
        preorder(root.left)
        preorder(root.right)

class Codec:
    head = None
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ret = []
        self._serialize(root, ret)
        return ret

    def _serialize(self, root, ret):
        if root is None:
            ret.append(None)
        else:
            ret.append(root.val)
            self._serialize(root.left, ret)
            self._serialize(root.right, ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        """
        Codec.head = None
        self._deserialize(data)
        return Codec.head
    def _deserialize(self,data):
        if len(data) == 0:
            return None
        else:
            val = data.pop(0)
            if val is None:
                return None
            node = TreeNode(val)
            if Codec.head is None:
                Codec.head = node
            node.left = self._deserialize(data)
            node.right = self._deserialize(data)
            return node

# [1, 2, None, None, 3, 4, None, None, 5, None, None]
# 先根遍历的编码方式
build_obj = Codec()
head = build_obj.deserialize([5,3,2,None,None,4,None,None,6,None,7])
# head = build_obj.deserialize([3,1,None,2,4])
preorder(head)
print()


#########################################################################

def num2char(num):
    return chr( num + ord('a'))
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        ret = []
        self.dfs(root, [], ret)
        # print(ret)
        ret = sorted(ret)
        if len(ret) != 0:
            return ret[0]

    def dfs(self, root, state_lst, ret):
        if root is None:
            return
        if root.left is None and root.right is None:
            t = state_lst + [num2char(root.val)]
            ret.append("".join(t[::-1]))
            return
        self.dfs(root.left, state_lst + [num2char(root.val), ], ret)
        self.dfs(root.right, state_lst + [num2char(root.val), ], ret)



#########################################################################

build_obj = Codec()
# head = build_obj.deserialize([0,1,3,None,None,4,None,None, 2,3,None,None,4])
head = build_obj.deserialize([0, None, 1])
# head = build_obj.deserialize([3,1,None,2,4])
preorder(head)
print()

print(Solution().smallestFromLeaf(head))
