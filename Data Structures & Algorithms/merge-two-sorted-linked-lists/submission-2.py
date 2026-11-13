# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        iter1 = list1
        iter2 = list2
        actual_head = ListNode()
        actual_node = actual_head
        while iter1 and iter2:
            if iter1.val > iter2.val:
                actual_node.next = iter2
                iter2 = iter2.next
            else:
                actual_node.next = iter1
                iter1 = iter1.next
            
            actual_node = actual_node.next
        
        while iter1:
            actual_node.next = iter1
            iter1 = iter1.next
            actual_node = actual_node.next
        
        while iter2:
            actual_node.next = iter2
            iter2 = iter2.next
            actual_node = actual_node.next
        
        return actual_head.next
            
            
     
        