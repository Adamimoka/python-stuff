import random
board_side_length = 4
target_sum = 34


failed = False

while True:
    nums = [2,3,4,5,6,7,8,9,10,12,13,14,15,16]
    board = [[1,0,0,0],[0,11,0,0],[0,0,0,0],[0,0,0,0]]
    failed = False
    failures = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                randnum = random.choice(nums)
                board[row][col] = randnum
                nums.remove(randnum)
    #CHECK:
    #row check
    for row in board:
        if sum(row) != target_sum:
            failed = True
            failures.append("row check")
            break
    #column check
    for i in range(4):
        for j in range(4):
            if sum([board[j][i]]) != target_sum:
                failed = True
                failures.append("col check")
                break
    # diagonal check
    if sum([board[i][i] for i in range(4)]) != target_sum:
        failed = True 
        failures.append("diagonal 1")
    if sum([board[3-i][i] for i in range(4)]) != target_sum:
        failed = True 
        failures.append("diagonal 2")
    
 
    if failed:
        print(board)
        print(failures)
        break
    else:
        print("we done it")
        print(board)
        break
