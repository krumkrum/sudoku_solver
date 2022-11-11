import random
from math import sqrt


def compile_sudoku():
    pass


def fill_field():
    pass


class SudokuPart:
    def __init__(self, n):
        self.n = n
        self.field = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.max_number = int(self.n * self.n)
        self.valid_field_sum = sum([num for num in range(self.max_number)])

    def get_field_sum(self):
        return sum([sum(row) for row in self.field])

    def compile_sum(self):
        if self.get_field_sum() == self.valid_field_sum:
            return True
        else:
            return False

    def compile_copy(self):
        n = []
        for field in self.field:
            n += field
        visited = set()
        dup = [x for x in n if x in visited or (visited.add(x) or False)]

        if dup is []:
            return True

        else:
            return False

    def set_value(self, x, y, value):
        if self.valid_set(value):
            self.field[x][y] = value
        else:
            return False
        # raise Exception("Error with set value")

    def valid_set(self, value):
        if value < 0 or value > 9:
            return False
        for row in self.field:
            for field_value in row:
                if value == field_value:
                    return False
                else:
                    return True

    def get_value(self, x, y):
        return self.field[x][y]


# Create Sudoku Field by NxN size
class SudokuField:
    def __init__(self, n=9):
        self.N = n
        self.n = sqrt(self.N)
        if self.n.is_integer():
            self.n = int(self.n)
        else:
            raise Exception("This not trivial case, use SudokuField.py for compile this case")
        self.sp = SudokuPart(self.n)
        self.parts = [[SudokuPart(self.n) for _ in range(self.n)] for _ in range(self.n)]

    def get_print_row(self, row_len_value):
        s = "_" * row_len_value + " "
        return s * self.n

    def print_field(self):
        for i in range(self.n):
            print(self.get_print_row(9))
            for j in range(self.n):
                print(self.parts[i][j].field[j], self.parts[i][j].field[j], self.parts[i][j].field[j])

    def compile_row(self, row_num=0):
        pass

    def compile_col(self):
        pass

    def fill_field(self):
        first_value = 2
        second_value = 3
        for i in range(self.sp.max_number):
            pass


if __name__ == '__main__':
    SIZE = 9
    SF = SudokuField(SIZE)
    SF.print_field()

