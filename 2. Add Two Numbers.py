#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 14:05:33 2025

@author: tom
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_length(l):
    n = l
    length = 1
    while n.next != None:
        n = n.next
        length += 1
    return length


def get_num(l, l1_length):
    n = l
    running_sum = 0
    i = 0

    while n != None:
        print(n.val)
        running_sum += n.val * 10 ** (i)
        n = n.next
        i += 1
    
    return running_sum

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1_length = get_length(l1)
        l2_length = get_length(l2)
        
        l1_num = get_num(l1, l1_length)
        l2_num = get_num(l2, l2_length)

        l_sum_num = l1_num + l2_num
        
        l = None
        for val_str in str(l_sum_num):
            l = ListNode(int(val_str), next=l) 

        return l