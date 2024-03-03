from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head

        for _ in range(n):
            fast = fast.next

        if fast is None:
            return head.next

        fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head