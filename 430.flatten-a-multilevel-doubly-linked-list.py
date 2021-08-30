"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        if not head.child:
            head.next=self.flatten(head.next)
        else:
            childLevel=self.flatten(head.child)
            childLevel.prev=head
            p=childLevel
            while p.next:
                p=p.next
                p.child=None
            if head.next:
                head.next.prev=p
                p.next=head.next
                head.next=childLevel
            else:
                head.next=childLevel
                childLevel.prev=head
            head.child=None
        return head
# @lc code=end