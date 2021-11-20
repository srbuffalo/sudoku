import pygame
import solver
import time
import copy
import sys
# it's not recommended to change any number if you don't understand the codes, most numbers are related to the size of interfaces, so change it might leads to a more ugly interface. 


class SuDu:
    pygame.init()
    pygame.display.set_caption("sudoku")

    def __init__(self, screen=pygame.display.set_mode([450, 510]), font=pygame.font.SysFont("comicsans", 35), board=None):
        self.screen = screen
        self.font = font      # font of numbers in grid
        self.time_font = pygame.font.SysFont("comicsans", 40)  # font of time
        self.solver = solver.Solver()
        for row in range(9):
            for column in range(9):
                if board[row][column] == 0:
                    board[row][column] = ' '
        self.answer = self.solver.answer(copy.deepcopy(board))
        self.current_grid = None
        self.sudo(board)

    # initialize the original sudoku grids
    def draw(self, board):
        self.screen.fill((255, 255, 255))        # change the background color to white

        for each in range(1, 10):    # draw lines for sudo
            if each % 3 != 0:
                pygame.draw.line(self.screen, (200, 200, 200), (0, 50 * each), (450, 50 * each), 1)
                pygame.draw.line(self.screen, (200, 200, 200), (50 * each, 0), (50 * each, 450), 1)
            else:
                pygame.draw.line(self.screen, (255, 0, 0), (0, 50 * each), (450, 50 * each), 2)
                pygame.draw.line(self.screen, (255, 0, 0), (50 * each, 0), (50 * each, 450), 2)

        for row in range(9):   # fill immutable grid with number
            for column in range(9):
                if board[row][column] != ' ':
                    kg = self.font.render("%d" % board[row][column], True, (200, 200, 200))
                    g = kg.get_rect()
                    g.center = (column * 50 + 25, row * 50 + 25)
                    self.screen.blit(kg, g)
        pygame.display.update()

    # change color of grid that was clicked
    def choose(self, row, column, board):
        colors = [(255, 0, 0), (200, 200, 200), (200, 200, 200)]
        # change background color of previous chosen grid so there will be only one chosen grid
        if self.current_grid and self.current_grid != [row, column]:
            v = board[self.current_grid[0]][self.current_grid[1]]
            kg = pygame.Surface([50, 50])
            kg.fill((255, 255, 255))
            g = kg.get_rect(topleft=(self.current_grid[1] * 50, self.current_grid[0] * 50))
            self.screen.blit(kg, g)
            kg = self.font.render("%s" % v, True,
                                  (0, 0, 0) if v == self.answer[self.current_grid[0]][self.current_grid[1]] else (
                                  255, 0, 0))
            g = kg.get_rect()
            g.center = (self.current_grid[1] * 50 + 25, self.current_grid[0] * 50 + 25)
            self.screen.blit(kg, g)
            pre_up, pre_down = self.current_grid[0], self.current_grid[0] + 1
            pre_left, pre_right = self.current_grid[1], self.current_grid[1] + 1
            for side in [pre_up, pre_down]:  # change color of sides of previous grid
                if side != 0:
                    pygame.draw.line(self.screen, colors[side % 3], (pre_left * 50, side * 50),
                                     (pre_right * 50, side * 50),
                                     1 if side % 3 != 0 else 2)
            for side in [pre_left, pre_right]:
                if side != 0 and side != 9:
                    pygame.draw.line(self.screen, colors[side % 3], (side * 50, pre_up * 50),
                                     (side * 50, pre_down * 50),
                                     1 if side % 3 != 0 else 2)
        pv = board[row][column]  # memorize the current grid's previous number(if there was one) so we can change background color of chosen grid and put it on the top of chosen grid before we enter a new number
        up, down = row, row + 1
        left, right = column, column + 1
        g = pygame.surface.Surface([50, 50]).get_rect(topleft=(column * 50, row * 50))
        background = pygame.Surface([50, 50])
        background.fill((248, 248, 255))
        self.screen.blit(background, g)
        kg = self.font.render(f'{pv}', True, (0, 0, 0) if pv == self.answer[row][column] else (255, 0, 0))
        g = kg.get_rect()
        g.center = (column * 50 + 25, row * 50 + 25)
        self.screen.blit(kg, g)
        for side in [up, down]:  # change color of sides of chosen grid
            if side != 0:
                pygame.draw.line(self.screen, colors[side % 3], (left * 50, side * 50), (right * 50, side * 50),
                                 1 if side % 3 != 0 else 2)
        for side in [left, right]:
            if side != 0 and side != 9:
                pygame.draw.line(self.screen, colors[side % 3], (side * 50, up * 50), (side * 50, down * 50),
                                 1 if side % 3 != 0 else 2)
        self.current_grid = [row, column]
        pygame.display.update()

    # fill a mutable grid with entered number
    def fill(self, board, number):
        row, column = self.current_grid[0], self.current_grid[1]
        if not number:
            return
        if number == "del":
            colors = [(255, 0, 0), (200, 200, 200), (200, 200, 200)]
            up, down = row, row + 1
            left, right = column, column + 1
            grid = pygame.Surface([50, 50])
            grid.fill((255, 255, 255))
            self.screen.blit(grid, (column * 50, row * 50))
            for side in [up, down]:  # change color of sides of chosen grid
                if side != 0:
                    pygame.draw.line(self.screen, colors[side % 3], (left * 50, side * 50), (right * 50, side * 50),
                                     1 if side % 3 != 0 else 2)
            for side in [left, right]:
                if side != 0 and side != 9:
                    pygame.draw.line(self.screen, colors[side % 3], (side * 50, up * 50), (side * 50, down * 50),
                                     1 if side % 3 != 0 else 2)
            board[row][column] = ' '
            pygame.display.update()
            return
        board[row][column] = number
        # if the entered number is correct, its color will be black, otherwise, it will be red
        if number == self.answer[row][column]:
            kg = self.font.render(f"{number}", True, (0, 0, 0))
        else:
            kg = self.font.render(f"{number}", True, (255, 0, 0))
        # cover the chosen grid with blank so that it looks like the value was changed rather than overlap
        g = pygame.surface.Surface([35, 35]).get_rect(center=(column * 50 + 25, row * 50 + 25))
        background = pygame.Surface([35, 35])
        background.fill((248, 248, 255))
        self.screen.blit(background, g)
        # put new number on the top of chosen grid
        g = kg.get_rect()
        g.center = (column * 50 + 25, row * 50 + 25)
        self.screen.blit(kg, g)
        pygame.display.update(g)

    # show the answer
    def fill_automatic(self, board, immutable):
        for row in range(9):
            for column in range(9):
                if not immutable[(row, column)]:
                    if board[row][column] != self.answer[row][column]:
                        background = pygame.Surface([35, 35])
                        background.fill((255, 255, 255))
                        g = background.get_rect(center=(column * 50 + 25, row * 50 + 25))
                        self.screen.blit(background, g)
                        kg = self.font.render("%s" % self.answer[row][column], True, (0, 0, 0))
                        g = kg.get_rect()
                        g.center = (column * 50 + 25, row * 50 + 25)
                        self.screen.blit(kg, g)
                        pygame.display.update(g)
                        immutable[(row, column)] = True

    # update gaming time
    def draw_time(self, start):
        run_time = time.time() - start
        if run_time < 60:
            kg = self.time_font.render("time:    " + str(int(run_time) % 60), True, (0, 0, 0))
        else:
            kg = self.time_font.render("time:  " + str(int(run_time) // 60) + ":" + str(int(run_time) % 60), True, (0, 0, 0))
        g = kg.get_rect(topleft=(300, 470))
        pygame.draw.rect(self.screen, (255, 255, 255), g, 37)
        self.screen.blit(kg, g)
        pygame.display.update(g)

    def sudo(self, board):
        immutable = {}
        for row in range(9):
            for column in range(9):
                if board[row][column] != ' ':
                    immutable[(row, column)] = True
                else:
                    immutable[(row, column)] = False
        start = time.time()
        self.draw(board)
        ft = pygame.font.SysFont("comicsans", 40)
        kg = ft.render("time:    0", True, (0, 0, 0))
        g = kg.get_rect()
        g.topleft = (300, 470)
        self.screen.blit(kg, g)
        running = True
        row = None
        column = None
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame. MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // 50
                    row = pos[1] // 50
                    if row < 9 and column < 9:
                        if not immutable[(row, column)]:
                            self.choose(row, column, board)

                if event.type == pygame.KEYDOWN:
                    key = ''
                    if 48 < event.key < 58:
                        key = event.key - 48
                    elif event.key == pygame.K_SPACE:
                        self.fill_automatic(board, immutable)
                    elif event.key == pygame.K_DELETE:
                        key = 'del'
                    if row != None and column != None and not immutable[(row, column)]:
                        self.fill(board, key)
            self.draw_time(start)

        pygame.quit()
        sys.exit()
