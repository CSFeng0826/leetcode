# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class ListNode:
     def __init__(self, x, _next=None):
         self.val = x
         self.next = _next
         
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        temp = ans
        while True:
            carry = False
            if l1 == None and l2 == None:
                break
            elif l1 == None:
                temp.next = ListNode(l2.next.val)
            elif l2 == None:
                temp.next = ListNode(l1.next.val)
            else:
                _sum = l1.val + l2.val
                temp.val = _sum % 10
                if _sum // 10 > 0:
                    carry = True
                else:
                    carry = False
                temp.next = ListNode(0)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        return ans

l1 = ListNode(2, ListNode(3, ListNode(1)))
l2 = ListNode(1, ListNode(4, ListNode(5)))

s = Solution()
ans = s.addTwoNumbers(l1, l2)

while ans != None:
    print(ans.val)
    ans = ans.next