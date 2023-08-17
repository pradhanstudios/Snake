from packages.consts import *


class Node:
    def __init__(self, x: int, y: int):
        self.coord = (x, y)
        self.next = None


class Snake:
    def __init__(self):
        self.head = Node(NUM_COLS // 2, NUM_ROWS // 2)
