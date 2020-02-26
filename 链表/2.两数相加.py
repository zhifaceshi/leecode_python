#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def ___repr__(self):
        return f"node {self.val} -> {self.next.val if self.next != None else None}"
    def __str__(self):
        return self.__repr__()

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        t1 = l1
        t2 = l2
        c = 0
        head = ListNode(0)
        pre = None
        while t1 != None and t2 != None:
            value = t1.val + t2.val + c
            c = value // 10
            v = value % 10
            cur_node = ListNode(v)
            if head.next == None:
                head.next = cur_node
            if pre is None:
                pre = cur_node
            else:
                pre.next = cur_node
                pre = cur_node
            t1 = t1.next
            t2 = t2.next
            
        while t1 != None:
            value = t1.val + c
            c = value // 10
            v = value % 10
            node = ListNode(v)
            pre.next = node
            pre = node
            t1 = t1.next
        while t2 != None:
            value = t2.val + c
            c = value // 10
            v = value % 10
            node = ListNode(v)
            pre.next = node
            pre = node
            t2 = t2.next
        if c != 0:
            pre.next = ListNode(c)
        return head.next




# @lc code=end
if __name__ == "__main__":
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

    l1 = [9, 8]
    l2 = [1, ]
    l1 = construct_node(l1)
    l2 = construct_node(l2)
    a = Solution().addTwoNumbers(l1, l2)
    showList(a)