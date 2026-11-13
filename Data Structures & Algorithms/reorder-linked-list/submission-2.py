# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # first lets find the middle node
        slow = head
        if not slow.next or not slow.next.next:
            print(head.val)
            return
        
        fast = slow.next.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next

        # lets reverse the second half of the list
        current = mid.next
        prev = None
        mid.next = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        head_2 = prev
        p1, p2 = head, head_2
        while p1 and p2:
            p1_next = p1.next
            p2_next = p2.next
            p1.next = p2
            p2.next = p1_next
            p1 = p1_next
            p2 = p2_next
        
        
        current = head
        while current is not None:
            print(current.val)
            current = current.next