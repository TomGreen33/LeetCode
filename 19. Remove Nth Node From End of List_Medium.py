# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Get the length of the list
        length = 1
        node = head
        while node.next != None:
            node = node.next
            length += 1

        if length == 1:
            head = None
        elif n == length:
            head = head.next
        else:
            # Find the index of the item to remove
            remove_idx = length - n
            
            
            # Traverse to the item before the item to be removed
            node = head
            for i in range(remove_idx-1):
                node = node.next
            
            # Remove the item
            next_node = node.next
            node.next = next_node.next

        return head