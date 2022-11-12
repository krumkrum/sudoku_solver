import tkinter
import tkinter as tk
import tkinter.ttk as ttk


class SudokuMonitor:
    def __init__(self, window_size='700x470', field=None):
        self.main = tk.Tk()

        self.ControlLabel = ControlLabel()
        self.field = field
        self.SN = SudokuNumField(control_label=self.ControlLabel)
        self.SC = SudokuControlField(control_label=self.ControlLabel)

        self.pack_sudoku_control_label()
        self.pack_sudoku_btns()
        self.pack_control_btns()

        self.main.geometry(window_size)

    def pack_sudoku_control_label(self):
        self.ControlLabel.place(x=550, y=200)

    def pack_sudoku_btns(self):
        for y, row in enumerate(self.SN.field):
            for x, btn in enumerate(row):
                btn.place(x=(y * 50) + 5, y=(x * 50) + 5)

    def pack_control_btns(self):
        for y, row in enumerate(self.SC.field):
            for x, btn in enumerate(row):
                btn.place(x=(x * 50) + 500, y=(y * 50) + 5)

    def fill_field(self, field):
        for y, row in enumerate(self.SN.field):
            for x, btn in enumerate(row):
                btn.configure(text=(str(field[x][y])))


class SudokuNumField:
    def __init__(self, control_label=None):
        self.control_label = control_label
        self.field = [[ValueBtn(c_label=control_label) for _ in range(9)] for _ in range(9)]


class SudokuControlField:
    def __init__(self, control_label=None):
        self.control_label = control_label
        self.field = [[ControlBtn(c_label=control_label, value=i + 1 + (j * 3)) for i in range(3)] for j in range(3)]


class ControlLabel(tk.Label):
    def __init__(self, parent=None, value=0):
        super(ControlLabel, self).__init__(parent, text=" ")


class ControlBtn(tk.Button):
    def __init__(self, parent=None, value=1, c_label=None):
        super().__init__(parent, width=6, height=3, text=value, command=self.on_click)
        self.value = value
        self.label = c_label

    def on_click(self):
        self.label['text'] = str(self.value)


class ValueBtn(tk.Button):
    def __init__(self, parent=None, value=1, c_label=None):
        super().__init__(parent, width=6, height=3, command=self.on_click)
        self.label = c_label

    def on_click(self, value=None):
        if value:
            self["text"] = value
            return
        if self["text"] == self.label['text']:
            self["text"] = " "
        else:
            self["text"] = self.label['text']


if __name__ == '__main__':
    SM = SudokuMonitor()
