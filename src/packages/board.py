from packages.consts import *
from random import choice


class Board:
    def __init__(self) -> None:
        self.values = [EMPTY, SNAKE, FRUIT]
        self.board = [[EMPTY for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]
        self.free_spaces = []
        for y in range(NUM_ROWS):
            for x in range(NUM_COLS):
                self.free_spaces.append((x, y))
        self.fruit = choice(self.free_spaces)
        self.board[self.fruit[0]][self.fruit[1]] = FRUIT

    def print_board(self):
        print("BOARD:")
        for row in self.board:
            print(row)

    def update_free_spaces(self):
        for y in range(NUM_ROWS):
            for x in range(NUM_COLS):
                if self.board[x][y] == EMPTY:
                    self.free_spaces.append((x, y))

    def replace_fruit(self):
        self.board[self.fruit[0]][self.fruit[1]] = SNAKE
        self.fruit = choice(self.free_spaces)
        self.board[self.fruit[0]][self.fruit[1]] = FRUIT

    def spawn_fruit(self):
        self.fruit = choice(self.free_spaces)
        self.board[self.fruit[0]][self.fruit[1]] = FRUIT
