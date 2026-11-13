"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        old_new_mapper = {}
        iter1 = head
        while iter1:
            new_node = Node(iter1.val)
            old_new_mapper[iter1] = new_node
            iter1 = iter1.next
        
        print(old_new_mapper)
        
        iter1 = head
        while iter1:
            updated_node = old_new_mapper[iter1]
            updated_node.next = old_new_mapper[iter1.next] if iter1.next else None
            updated_node.random = old_new_mapper[iter1.random] if iter1.random else None
            iter1 = iter1.next
        
        return old_new_mapper[head]

            