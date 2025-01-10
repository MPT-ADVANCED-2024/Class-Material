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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        before_head = ListNode()
        before_head.next = head

        length = 1
        cur = head
        while cur.next is not None:
            cur = cur.next
            length += 1

        prev = before_head
        for _ in range((length - k) % length):
            prev = head
            head = head.next
        prev.next = None

        tail = head
        while tail.next is not None:
            tail = tail.next
        tail.next = before_head.next

        return head


head = to_linked_list([1, 2, 3, 4, 5])
head = Solution().rotateRight(head, 2)
print_linked_list(head)  # Expected: 4->5->1->2->3

head = to_linked_list([0, 1, 2])
head = Solution().rotateRight(head, 4)
print_linked_list(head)  # Expected: 2->0->1

head = to_linked_list([1, 2, 3, 4, 5])
head = Solution().rotateRight(head, 12)
print_linked_list(head)  # Expected: 4->5->1->2->3

head = to_linked_list([])
head = Solution().rotateRight(head, 100)
print_linked_list(head)  # Expected: (empty)
