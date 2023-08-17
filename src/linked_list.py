from packages.consts import *


class Node:
    def __init__(self, x: int, y: int) -> None:
        self.coord = (x, y)
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = Node(NUM_COLS // 2, NUM_ROWS // 2)


class Snake:
    def __init__(self) -> None:
        self.body = LinkedList()
