# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    

        current = head

        new_head = None
        previous_tail = None

        while current:

            # --------------------------------
            # 1. Check that k nodes exist
            # --------------------------------
            check = current

            for _ in range(k):

                if check is None:

                    # Not enough nodes left
                    return new_head if new_head else head

                check = check.next


            # --------------------------------
            # 2. Reverse exactly k nodes
            # --------------------------------
            group_head, group_tail, next_group = self.reverse(
                current, k
            )


            # --------------------------------
            # 3. First group sets new head
            # --------------------------------
            if new_head is None:
                new_head = group_head


            # --------------------------------
            # 4. Connect previous group
            # --------------------------------
            if previous_tail is not None:
                previous_tail.next = group_head


            # Connect this group to remaining list
            group_tail.next = next_group


            # --------------------------------
            # 5. Move to next group
            # --------------------------------
            previous_tail = group_tail
            current = next_group

        return new_head


    def reverse(self, start, k):

        prev = None
        curr = start

        for _ in range(k):

            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node

        return prev, start, curr
        