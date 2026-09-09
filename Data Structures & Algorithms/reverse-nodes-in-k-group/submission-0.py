# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 1:
            return head

        current = head

        new_head = None
        previous_group_tail = None

        while current:

            # --------------------------------
            # 1. Check if k nodes are available
            # --------------------------------
            kth = current

            for _ in range(k - 1):
                kth = kth.next

                # Fewer than k nodes remain
                if kth is None:
                    return new_head


            # Node after this group
            group_next = kth.next

            # Remember the first node
            # because it becomes the tail after reversal
            group_start = current


            # --------------------------------
            # 2. Reverse this group
            # --------------------------------
            prev = group_next

            while current != group_next:

                next_node = current.next

                current.next = prev

                prev = current
                current = next_node


            # --------------------------------
            # 3. Connect the reversed group
            # --------------------------------

            # First reversed group:
            # kth becomes the new head
            if new_head is None:
                new_head = kth

            # Connect previous group to this group
            if previous_group_tail is not None:
                previous_group_tail.next = kth


            # Original first node is now
            # the tail of this reversed group
            previous_group_tail = group_start


        return new_head
        