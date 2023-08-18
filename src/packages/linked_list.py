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

        # 4. If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

    def printll(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
