from pygame.rect import Rect
from packages.linked_list import LinkedList


class Player:
    def __init__(self, x, y, w, h, color: tuple[int]):
        self.body = LinkedList()
        self.body.insert((Rect(x, y, w, h), color))
        self.cur_player = self.body.head

    def __str__(self):  # for testing
        x, y, w, h = self.cur_player.data[0]
        color = self.cur_player.data[1]
        return "pos: %s, %s; size: %s %s; color: %s" % (x, y, w, h, color)
