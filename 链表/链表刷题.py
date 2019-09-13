import itertools
import collections
import math
import re
import sys

MAXINF = float('inf')
MININF = -float('inf')

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val)
def showList(node):
    while node != None:
        print(" " + str(node.val), end='')
        node = node.next
    print()
def construct_node(lst):
    head = None
    preNode = None
    for n in lst:
        node = ListNode(n)
        if head is None:
            head = node
        if preNode is not None:
            preNode.next = node
        preNode = node
    return head

# 蓄水池抽样算法
# https://www.cnblogs.com/hrlnw/archive/2012/11/27/2777337.html
# 每个元素都有k/x的概率被选中，然后等概率的（1/k）替换掉被选中的元素。其中x是元素的序号。
import random
# 蓄水池抽样证明
# http://sofasofa.io/forum_main_post.php?postid=1002998
class Solution:
    chizi = None
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        count = 1
        Solution.chizi = None
        while head != None:
            if (Solution.chizi)is None:
                Solution.chizi = head
            else:
                count += 1
                if random.random() < 1 / count:
                    Solution.chizi = head
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return Solution.chizi


# 构造节点
head = construct_node([1,2,3,-3,4])
t = Solution().sortList(head)
# 展示节点
showList(t)



