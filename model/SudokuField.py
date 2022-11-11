import random
import time
from random import randint as rn
from random import choice
import math


def compile_sudoku():
    pass


def fill_field():
    pass


# Create Sudoku Field by NxP size
class SudokuField:
    def __init__(self, n, p):
        self.N = n
        self.P = p

        self.field = [[0 for _ in range(self.N)] for _ in range(self.P)]
        self.max_number = math.sqrt(self.N)

    def print_field(self):
        for row in self.field:
            print(row)

    def fill_random(self):
        for y, row in enumerate(self.field):
            for x, value in enumerate(row):
                self.field[y][x] = random.randint(1, 9)

    def compile_field(self, row_num=0):
        arr_choose_value = [i + 1 for i in range(9)]
        x = y = 5

        choose_value = choice(arr_choose_value)
        arr_choose_value.remove(choose_value)

        choose_value2 = choice(arr_choose_value)
        arr_choose_value.remove(choose_value2)

        self.field[x][y] = choose_value

        for _ in range(1000):
            time.sleep(1)
            print("_" * len(str(self.field[0])))
            self.print_field()
            # fix value x
            if rn(1, 2) == 1:
                k = rn(0, 3)
                self.field[x][y + k] = choose_value

            # fix value y
            else:
                k = rn(0, 3)
                self.field[x + k][k] = choose_value


if __name__ == '__main__':
    size = [9, 9]
    SF = SudokuField(size[0], size[1])
    SF.fill_random()
    SF.print_field()
