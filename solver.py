#EasyBoard
#boardEasy = [
 #   [7,8,0,4,0,0,1,2,0],
 #   [6,0,0,0,7,5,0,0,9],
 #   [0,0,0,6,0,1,0,7,8],
 #   [0,0,7,0,4,0,2,6,0],
 #   [0,0,1,0,5,0,9,3,0],
 #   [9,0,4,0,6,0,0,0,5],
 #   [0,7,0,3,0,0,0,1,2],
 #   [1,2,0,0,0,7,4,0,0],
 #   [0,4,9,2,0,6,0,0,7]

#MediumBoard
#board = [
 #   [0,0,0,2,6,0,7,0,1],
 #  [6,8,0,0,7,0,0,9,0],
 #   [1,9,0,0,0,4,5,0,0],
 #  [8,2,0,1,0,0,0,4,0],
 #   [0,0,4,6,0,2,9,0,0],
 #   [0,5,0,0,0,3,0,2,8],
 #   [0,0,9,3,0,0,0,7,4],
 #   [0,4,0,0,5,0,0,3,6],
 #   [7,0,3,0,1,8,0,0,0]
#]

#HardBoard
board = [
    [0,2,0,0,0,0,0,0,0],
    [0,0,0,6,0,0,0,0,3],
    [0,7,4,0,8,0,0,0,0],
    [0,0,0,0,0,3,0,0,2],
    [0,8,0,0,4,0,0,1,0],
    [6,0,0,5,0,0,0,0,0],
    [0,0,0,0,1,0,7,8,0],
    [5,0,0,0,0,9,0,0,0],
    [0,0,0,0,0,0,0,4,0]
]




def prints_the_board(board):
    for a in range(len(board)):
        if a % 3 == 0 and a != 0:
            print("- - - - - - - - - - - -")

        for b in range(len(board[0])):
            if b % 3 == 0 and b != 0:
                print(" | ", end="")

            if b == 8:
                print(board[a][b])
            else:
                print(str(board[a][b]) + " ", end="")


prints_the_board(board)

def empty_spot(board):
    for c in range(len(board)):
        for d in range(len(board[c])):
            if board[c][d] == 0:
                return (c, d) # row, col

    return None


def validity(board, num, position):
    # check if the numbers in row
    for i in range(len(board[0])):
        if board[position[0]][i] == num and position[1] != i:
            return False

    # check if the numbers in col

    for j in range(len(board)):
        if board[j][position[1]] == num and position[0] != j:
            return False

    # check if the 3by3 cube does not have the same number

    box_x = position[0] // 3
    box_y = position[1] // 3

    for i in range(box_x * 3, box_x*3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
              if board[i][j] == num and (i, j) != position:
                  return False


    return True

def solve(board):
    find = empty_spot(board)
    if not find:
        return True
    else:
        row, col = find


    for i in range(1, 10):
        if validity(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


print("----------------------------")
solve(board)
prints_the_board(board)

