import sudoku
'''
Extension direction: 
1.use database to store information of sudoku boards(needs to be collected or created before starting a game) and corresponding answers, so it doesn't need to create answer everytime the game was initialized;
2.add functionality to create a random sudoku board, but in this case, it's pointless to store information in database, so this one will be slower that previous one.
'''
# easy one
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# hard one
board2 = [
    [0, 0, 9, 0, 0, 0, 0, 0, 6],
    [6, 3, 0, 0, 2, 0, 7, 0, 0],
    [0, 0, 8, 0, 0, 3, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 0],
    [4, 1, 0, 0, 0, 2, 0, 0, 8],
    [0, 0, 0, 0, 7, 0, 0, 5, 0],
    [0, 0, 0, 4, 0, 0, 8, 0, 0],
    [2, 6, 0, 0, 0, 1, 0, 0, 4],
    [9, 0, 0, 0, 0, 0, 0, 0, 0]
]

if __name__ == "__main__":
    sudo.SuDu(board=board)
