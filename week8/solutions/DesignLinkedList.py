from typing import Optional


class ListNode:
    def __init__(self, val: Optional[int] = None, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next: Optional[ListNode] = next


class MyLinkedList:

    def __init__(self):
        self.before_begin = ListNode()

    def get(self, index: int) -> int:
        cur = self.before_begin
        for _ in range(index):
            if cur.next is None:
                return -1
            cur = cur.next
        return cur.next.val if cur.next is not None else -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, self.before_begin.next)
        self.before_begin.next = new_node

    def addAtTail(self, val: int) -> None:
        cur = self.before_begin
        while cur.next is not None:
            cur = cur.next
        cur.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.before_begin
        for _ in range(index):
            if cur.next is None:
                return
            cur = cur.next
        new_node = ListNode(val, cur.next)
        cur.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        cur = self.before_begin
        for _ in range(index):
            if cur.next is None:
                return
            cur = cur.next
        if cur.next is not None:
            cur.next = cur.next.next

    def __str__(self) -> str:
        "for print to work"
        cur = self.before_begin
        result = []
        while cur.next is not None:
            cur = cur.next
            result.append(str(cur.val))
        return "->".join(result)


myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1), print(myLinkedList)  # 1
myLinkedList.addAtTail(3), print(myLinkedList)  # 1->3
myLinkedList.addAtIndex(1, 2), print(myLinkedList)  # 1->2->3
print(myLinkedList.get(1))  # 2
myLinkedList.deleteAtIndex(1), print(myLinkedList)  # 1->3
print(myLinkedList.get(1))  # 3
