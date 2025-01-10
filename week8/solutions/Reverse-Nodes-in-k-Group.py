from typing import Optional


class ListNode:
    def __init__(self, val: Optional[int] = None, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next: Optional[ListNode] = next


def to_linked_list(arr: list[int]) -> Optional[ListNode]:
    nodes = [ListNode(val) for val in arr]
    for i in range(1, len(nodes)):
        nodes[i - 1].next = nodes[i]
    return nodes[0] if nodes else None


def print_linked_list(first_node: Optional[ListNode]) -> None:
    cur = first_node  # a pointer to the "cur"rent node
    while cur is not None:
        print(cur.val, end="->" if cur.next is not None else "\n")
        cur = cur.next  # move to the next node


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        before_head = ListNode()
        before_head.next = head

        before_left, left = before_head, head
        while True:
            # check if there are at least k nodes left
            cur = before_left
            for _ in range(k):
                if cur.next is None:
                    return before_head.next
                cur = cur.next

            # reverse the current k nodes
            pre, cur = before_left, left
            for _ in range(k):
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next

            # connect the reversed k nodes properly
            before_left.next = pre
            left.next = cur

            # move to the next k nodes
            before_left, left = left, cur


head = to_linked_list([1, 2, 3, 4, 5])
head = Solution().reverseKGroup(head, 2)
print_linked_list(head)  # 2->1->4->3->5

head = to_linked_list([1, 2, 3, 4, 5])
head = Solution().reverseKGroup(head, 3)
print_linked_list(head)  # 3->2->1->4->5
