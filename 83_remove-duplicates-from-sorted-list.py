from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr = head

        while itr != None and itr.next != None:
            if itr.val == itr.next.val:
                itr.next = itr.next.next
            else:
                itr = itr.next

        return head


# you can do it, cheers!!!!