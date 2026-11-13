# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # approach
        # slow pointer starts at head whereas fast pointer starts at head + k
        # when fast pointer is at the end, slow pointer is at kth element from end
        # Then we will delete the element and move on
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        for _ in range(n+1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next


        