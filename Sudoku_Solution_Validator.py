# https://www.codewars.com/kata/529bf0e9bdf7657179000008/train/python

def valid_solution(board):
    # Check for zeros
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==0: return False

    # Check rows
    for row in board:
        numbers = []
        for number in row:
            if number in numbers or number > 9 or number < 1:
                return False
            numbers.append(number)

    # Check columns
    for i in range(len(board)):
        numbers = []
        for j in range(len(board[i])):
            number = board[j][i]
            if number in numbers or number > 9 or number < 1:
                return False
            numbers.append(number)

    # Check boxes
    for i in range(0, len(board), int(len(board)/3)):
        for j in range(0, len(board), int(len(board)/3)):
            numbers = []
            for k in range(int(len(board)/3)):
                for l in range(int(len(board)/3)):
                    number = board[i+k][j+l]
                    if number in numbers or number > 9 or number < 1:
                        return False
                    numbers.append(number)
    return True

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                      [6, 7, 2, 1, 9, 5, 3, 4, 8],
                      [7, 9, 8, 3, 4, 2, 5, 6, 1],
                      [8, 5, 9, 7, 6, 1, 4, 2, 3],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 6, 1, 5, 3, 7, 2, 8, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 4, 5, 2, 8, 6, 1, 7, 9]]), True);

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                      [6, 7, 2, 1, 9, 0, 3, 4, 9],
                      [1, 0, 0, 3, 4, 2, 5, 6, 0],
                      [8, 5, 9, 7, 6, 1, 0, 2, 0],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 0, 1, 5, 3, 7, 2, 1, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 0, 0, 4, 8, 1, 1, 7, 9]]), False);
