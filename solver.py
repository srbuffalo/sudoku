import pygame
import time


class Solver:
    def __init__(self):
        self.value = set([i for i in range(1, 10)])

    def possible_answer(self, raw, column, s):  # return possible answer set for a specific grid
        k = set()
        x = raw // 3
        y = column // 3
        for r in range(9):   # The values already in the same column
            if s[r][column] != " ":
                k.add(s[r][column])
        for c in range(9):  # The values already in the same raw
            if s[raw][c] != " ":
                k.add(s[raw][c])
        for r in range(x * 3, x * 3 + 3):   # The values already in the same 3*3 area
            for c in range(y * 3, y * 3 + 3):
                k.add(s[r][c])
        return self.value.difference(k)

    def solver(self, s):  # backtracking way to solve sudo
        for row in range(9):
            for column in range(9):
                if s[row][column] == ' ':
                    p = self.possible_answer(row, column, s)
                    if len(p) != 0:
                        for each in p:
                            s[row][column] = each
                            if self.solver(s):
                                return True
                        s[row][column] = ' '
                        return False
                    else:
                        return False
        return True

    def answer(self, s):  # create correct answer board and return
        self.solver(s)
        return s








