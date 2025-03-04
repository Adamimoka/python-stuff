from random import randint
from time import time
from pprint import pprint
rows = 8
cols = 8
board = [[' ' for _ in range(rows)] for _ in range(cols)]

def check_placement(board, row, col):
    for i in range(rows):
        if board[i][col] == 'Q':
            return False
    for i in range(cols):
        if board[row][i] == 'Q':
            return False
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'Q':
                if abs(i - row) == abs(j - col):
                    return False
    return True

def edit_board(board, row, col, piece):
   board[row][col] = piece

def remove_some_queens(board, num_queens):
    number_to_delete = randint(1, num_queens)
    deleted = 0
    while deleted < number_to_delete:
        r_x = randint(0, rows - 1)
        r_y = randint(0, cols - 1)
        if board[r_x][r_y] == 'Q':
            edit_board(board, r_x, r_y, ' ')
            deleted += 1
    return deleted

num_queens = 0
last_good = 0
best_board = []
best_queens = 0
start_time = time()
max_time = 4 # seconds
while True:
    r_x = randint(0, rows - 1)
    r_y = randint(0, cols - 1)
    if check_placement(board, r_x, r_y):
        edit_board(board, r_x, r_y, 'Q')
        num_queens += 1
    else:
        if last_good > 128:
            # looks like we're stuck, delete a random queen
            deleted = remove_some_queens(board,num_queens)
            num_queens -= deleted
            last_good = 0
        last_good += 1
        continue
    time_left = max_time - (time() - start_time)
    print(f"Best queens: {best_queens}, Time left: {time_left:.2f} seconds\r", end='')
    if num_queens > best_queens:
        best_queens = num_queens
        best_board = [row.copy() for row in board]
    if time() - start_time > max_time:
        break

pprint(best_board)
print(f"Best solution found in {time() - start_time:.3f} has {best_queens} queens.")