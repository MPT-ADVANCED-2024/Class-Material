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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        before_head = cur = ListNode()
        while l1 is not None or l2 is not None:
            x1, x2 = (l.val if l is not None else 0 for l in (l1, l2))
            val = x1 + x2 + carry

            carry = 0
            if val >= 10:
                val -= 10
                carry = 1

            cur.next = ListNode(val)
            cur = cur.next
            l1, l2 = (l.next if l is not None else None for l in (l1, l2))
        if carry:
            cur.next = ListNode(carry)
        return before_head.next


l1 = to_linked_list([2, 4, 3])
l2 = to_linked_list([5, 6, 4])
print_linked_list(Solution().addTwoNumbers(l1, l2))  # 7->0->8

l1 = to_linked_list([0])
l2 = to_linked_list([0])
print_linked_list(Solution().addTwoNumbers(l1, l2))  # 0

l1 = to_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = to_linked_list([9, 9, 9, 9])
print_linked_list(Solution().addTwoNumbers(l1, l2))  # 8->9->9->9->0->0->0->1
