'''
Advantages:
1. Insertion and deletion with a given location is O(1)
2. Is resizable. Grows and shrinks 

Disadvantages:
1. O(n) traversal because it is not contiguous in memory
2. 
'''

# CTCI 2.6

# Palindrome: Implement a function to check if a linked list is a palindrome.

# Madam

'''
use a stack
Run thru LL
Insert el to Stack
Run through Stack and pop to a string

base case: empty => root
reducer
'''

import sys
 

import sys
import os
 
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)

from Linkedlists import ListNode, Builder

def isPalindrome(root: ListNode):
    content = []
    curr = root
    while curr != None:
        content.append(curr.val)
        curr = curr.next
    print(content)
    print(content.reverse())
    return content == content[::-1]

builder_obj = Builder
head = builder_obj.build(['m', 'a', 'd', 'a', 'm'])
print("is palindrome", isPalindrome(head))
