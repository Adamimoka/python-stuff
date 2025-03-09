from random import choice
from time import time
board_side_length = 4
target_sum = board_side_length * (board_side_length**2 + 1) / 2

checks = 0

start_time = time()

def check_board(board, target_sum):
    #row check
    for row in board:
        if sum(row) != target_sum:
            return False
    
    #column check
    for i in range(board_side_length):
        if sum([board[j][i] for j in range(board_side_length)]) != target_sum:
            return False
    
    # diagonal check
    if ((sum([board[i][i] for i in range(board_side_length)]) != target_sum) or
        sum([board[board_side_length-1-i][i] for i in range(board_side_length)]) != target_sum):
        return False

    return True  

while True:
    nums = list(range(1, board_side_length**2 + 1))
    board = [[0 for _ in range(board_side_length)] for _ in range(board_side_length)]
    
    # fill in the board randomly
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                randnum = choice(nums)
                board[row][col] = randnum
                nums.remove(randnum)
    
    succeeded = check_board(board, target_sum)
 
    if succeeded:
        print("We did it after " + str(checks) + " checks. Took " + str(time() - start_time) + " seconds")
        print(board)
        break
    else:
        checks += 1
        if checks % 100000 == 0:
            print(f"Failed check {checks//100000} hundred thousand times")
            print(board)


# we done it after 631025066 checks, ~2 hours
# [[4, 16, 1, 13], [9, 5, 12, 8], [14, 2, 15, 3], [7, 11, 6, 10]]