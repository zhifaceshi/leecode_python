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

def get_node(head, val):
    while head is not None and head.val != val:
        head = head.next
    return head

##########################################################################################

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while slow != None and fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if slow is None or fast is None or fast.next is None:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast

head = construct_node([3,2,0,-4])
node = get_node(head, -4)
node.next = head.next

print(Solution().detectCycle(head), type(Solution().detectCycle(head)))