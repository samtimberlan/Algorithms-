# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack, curr = [], head

        while curr:
            if curr.val == n and stack:
                prev = stack.pop()
                prev.next = curr.next
            
            stack.append(curr)
            
            curr = curr.next

# [1,2,3,4,5], n = 2
class Builder:
    def build(arr: list):
        curr = dummy = ListNode()

        for el in arr:
            curr.next = ListNode(el)
            curr = curr.next
        return dummy.next

builder_obj = Builder
head = builder_obj.build([1,2,3,4,5])

sol_obj = Solution()
print(sol_obj.removeNthFromEnd(head=head, n=2))