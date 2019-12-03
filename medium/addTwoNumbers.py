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
        carry = 0
        while l1 != None or l2 != None:
            if l1 == None:
                _sum = l2.val + carry
                temp.val = (_sum % 10)
                l2 = l2.next
            elif l2 == None:
                _sum = l1.val + carry
                temp.val = (_sum % 10)
                l1 = l1.next
            else:
                _sum = l1.val + l2.val + carry
                temp.val = (_sum % 10)
                l1 = l1.next
                l2 = l2.next
                
            carry = _sum // 10  
            if l1 != None or l2 != None:
                temp.next = ListNode(0)
                temp = temp.next
            else:
                break  
            
        if carry > 0:
            temp.next = ListNode(carry)
        return ans

l1 = ListNode(1)
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

s = Solution()
ans = s.addTwoNumbers(l1, l2)

while ans != None:
    print(ans.val)
    ans = ans.next