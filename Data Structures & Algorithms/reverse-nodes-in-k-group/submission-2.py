# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        current = head

        final_head = None
        previous_tail = None

        while current:

            # Check if k nodes are available
            check = current

            for _ in range(k):

                if check is None:

                    # Connect leftover nodes
                    if previous_tail:
                        previous_tail.next = current

                    return final_head if final_head else head

                check = check.next


            # Reverse current group
            group_head, group_tail, next_group = self.reverse(current, k)


            # First reversed group becomes overall head
            if final_head is None:
                final_head = group_head


            # Connect previous group to this group
            if previous_tail:
                previous_tail.next = group_head


            # Connect this group to whatever comes next
            group_tail.next = next_group


            # Move forward
            previous_tail = group_tail
            current = next_group

        return final_head

    def reverse(self, head, k):

        prev = None
        curr = head

        for _ in range(k):

            next_node = curr.next

            curr.next = prev

            prev = curr
            curr = next_node

        return prev, head, curr