from . import player as p

class Node:
    def __init__(self, data: p.Player, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def insert(self, data: p.Player):
        new_node = Node(data)

        # new node as head
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def printll(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def next(self):
        self.head = self.head.next

