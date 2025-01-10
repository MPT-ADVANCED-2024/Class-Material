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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # create a dummy node to mark the head of this list
        before_head = ListNode()
        before_head.next = head

        # find the left most node and the node before it
        before_left = before_head
        left_node = head
        for _ in range(left - 1):
            before_left = left_node
            left_node = left_node.next

        # reverse the nodes between left and right
        right_node = before_left
        after_right = left_node
        for _ in range(right - left + 1):
            next = after_right.next
            after_right.next = right_node
            right_node = after_right
            after_right = next

        # connect the left node to the node after right
        left_node.next = after_right
        # connect the node before left to the right node
        before_left.next = right_node

        return before_head.next


head = to_linked_list([1, 2, 3, 4, 5])
rev = Solution().reverseBetween(head, 2, 4)
print_linked_list(rev)  # 1->4->3->2->5

head = to_linked_list([1, 2, 3, 4, 5])
rev = Solution().reverseBetween(head, 1, 4)
print_linked_list(rev)  # 4->3->2->1->5
