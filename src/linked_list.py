from packages.consts import *
# from pygame.rect import Rect


class Node:
    def __init__(self, xy: tuple[int], next=None) -> None:
        self.coord = xy
        self.next = next


class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def insert(self, data):
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
            print(temp.coord)
            temp = temp.next

    


# class Snake:
#     def __init__(self, x, y, w, h) -> None:
#         self.body = LinkedList(Rect(x, y, w, h))

#     def draw_body(self):
        
    
