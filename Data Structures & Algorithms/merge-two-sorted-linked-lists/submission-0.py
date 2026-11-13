# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        node_1 = list1
        node_2 = list2
        
        while node_1 is not None and node_2 is not None:
            if node_1.val > node_2.val:
                current.next = node_2
                node_2 = node_2.next
            else:
                current.next = node_1
                node_1 = node_1.next
            
            current = current.next
        
        if node_1:
            current.next = node_1
        
        if node_2:
            current.next = node_2
        
        return head.next


        