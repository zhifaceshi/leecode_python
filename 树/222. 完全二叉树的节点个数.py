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
#https://leetcode-cn.com/problems/delete-node-in-a-bst/solution/yong-qian-qu-huo-zhe-hou-ji-jie-dian-zi-shu-dai-ti/

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# # 方法1：用左子树中最大结点的代替被删除结点
#
#
# class Solution:
#     def deleteNode(self, root, key):
#         if root is None:
#             return None
#
#         if key < root.val:
#             root.left = self.deleteNode(root.left, key)
#             return root
#
#         if key > root.val:
#             root.right = self.deleteNode(root.right, key)
#             return root
#
#         if root.left is None:
#             new_root = root.right
#             root.right = None
#             return new_root
#
#         if root.right is None:
#             new_root = root.left
#             root.left = None
#             return new_root
#
#         # 找到左子树中最大的
#         predecessor = self.__maximum(root.left)
#         predecessor_copy = TreeNode(predecessor.val)
#         predecessor_copy.left = self.__remove_max(root.left)
#         predecessor_copy.right = root.right
#         root.left = None
#         root.right = None
#         return predecessor_copy
#
#     def __remove_max(self, node):
#         if node.right is None:
#             new_root = node.left
#             node.left = None
#             return new_root
#         node.right = self.__remove_max(node.right)
#         return node
#
#     def __maximum(self, node):
#         while node.right:
#             node = node.right
#         return node

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
#########################################################################

print(Solution().countNodes(head))