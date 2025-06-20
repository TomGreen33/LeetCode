#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 15:43:37 2025

@author: tom
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
       # Definition for singly-linked list.

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            out = head     
        elif head.next is None:
            out = head
        else:
            prev_node = head
            node = head
            next_node = node.next
            
            
            reset_head = True
            
            
            while True:
                
                try:
                    next_next_node = next_node.next
                except:
                    break
                
                try:
                    if next_node.next.next is not None:
                        node.next = next_node.next.next
                    else:
                        node.next = next_node.next
                except:
                    node.next = next_node.next

                    
                next_node.next = node

                if reset_head:
                    head = next_node
                    reset_head = False
                
                node = next_next_node
                
                if node is not None:
                    next_node = node.next 

                else:
                    break
        return head
                
