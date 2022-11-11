import time

import visualization.TkSudokuMonitor as SMonitor
import model.SudokuField as SField

SUDOKU_SIZE = [9, 9]
SUDOKU_MONITOR_SIZE = "700x470"


class Sudoku:
    def __init__(self):
        self.SField = SField.SudokuField(SUDOKU_SIZE[0], SUDOKU_SIZE[1])
        self.SField.fill_random()
        self.SField.print_field()

        self.SMonitor = SMonitor.SudokuMonitor()
        self.SMonitor.fill_field(self.SField.field)
        self.SMonitor.main.mainloop()


if __name__ == '__main__':
    sudoku = Sudoku()
