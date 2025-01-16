# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack, curr = [], head

        while curr:
            if curr.val == n and stack:
                prev = stack.pop()
                prev.next = curr.next
            
            stack.append(curr)
            
            curr = curr.next
    
    def count(self, head):
        curr, count = head, 1

        while curr:
            count += 1
            curr = curr.next
        return count
    
    def reverse(self, head):
        if not head or not head.next: return head
        prev = head

        curr = self.reverse(prev.next)
        prev.next.next = prev
        prev.next = None

        return curr
    
    def print_list(self, head):
        while head:
            print(head.val)
            head = head.next



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

llist = LinkedList()
print('print out', llist.print_list(head))
print('remove nth from end', llist.removeNthFromEnd(head=head, n=2))
print('count', llist.count(head))
print(llist.reverse(head))
print('print out', llist.print_list(head))



#def merge_sorted_linkedlists():