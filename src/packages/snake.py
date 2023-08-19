from pygame.rect import Rect
from packages.linked_list import LinkedList


class Snake:
    def __init__(self, xy: tuple):
        self.body = LinkedList()
        self.body.insert(xy)
        self.cur_player = self.body.head

    def __str__(self):  # for testing
        x, y, w, h = self.cur_player.data[0]
        color = self.cur_player.data[1]
        return "pos: %s, %s; size: %s %s; color: %s" % (x, y, w, h, color)

    def add_cell(self, xy: tuple):
        self.body.insert(xy)
