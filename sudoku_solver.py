import numpy
import time

board = [[0, 0, 3, 0, 0, 0, 1, 0, 0], 
         [0, 2, 0, 0, 6, 0, 0, 4, 0], 
         [4, 0, 0, 2, 0, 9, 0, 0, 7],
         [0, 0, 0, 8, 0, 1, 0, 0, 0],
         [0, 0, 4, 0, 0, 0, 8, 0, 0], 
         [7, 0, 0, 9, 0, 5, 0, 0, 4], 
         [0, 8, 0, 3, 6, 9, 0, 2, 0], 
         [3, 0, 0, 0, 5, 0, 0, 0, 1], 
         [0, 0, 0, 1, 0, 2, 0, 0, 0]]


def find_zeros(board):
    zeroes=[]
    for row in board:
        colIndex = 0
        x = board.index(row)
        for value in row:    
            colIndex +=1
            if value == 0:
                zeroes.append([x,colIndex-1])
                #print([x,colIndex-1])
    #print(zeroes) #51 zeroes
    return(zeroes)
        
#find_zeros(board)

def is_valid(board, row, col, value):
    #row
    check_row = (value in board[row])
    #print(board[row]) // True if Value is in row

    #col
    column = []
    x=0
    for line in board:
        column.append(board[x][col])
        x+=1
    check_col = value in (column) # True if value is in col
    #print(column)
    
    #3x3
    square1 = []
    square2 = []
    square3 = []
    square4 = []
    square5 = []
    square6 = []
    square7 = []
    square8 = []
    square9 = []

    for arrays in range(0,3):
       for units in range(0,3):
            square1.append(board[arrays][units])
       for units in range(3,6):
            square2.append(board[arrays][units])
       for units in range(6,9):
            square3.append(board[arrays][units])
    
    for arrays in range(3,6):
       for units in range(0,3):
            square4.append(board[arrays][units])
       for units in range(3,6):
            square5.append(board[arrays][units])
       for units in range(6,9):
            square6.append(board[arrays][units])
    
    for arrays in range(6,9):
       for units in range(0,3):
            square7.append(board[arrays][units])
       for units in range(3,6):
            square8.append(board[arrays][units])
       for units in range(6,9):
            square9.append(board[arrays][units])
    

    if (0<=row<3 and 0<=col<3):
        check3x3 = (value in square1)
    elif (0<=row<3 and 3<=col<6):
        check3x3 = (value in square2)
    elif (0<=row<3 and 3<=col<9):
        check3x3 = (value in square3)
    elif (3<=row<6 and 0<=col<3):
        check3x3 = (value in square4)                
    elif (3<=row<6 and 3<=col<6):
        check3x3 = (value in square5)
    elif (3<=row<6 and 6<=col<9):
        check3x3 = (value in square6)
    elif (6<=row<9 and 0<=col<3):
        check3x3 = (value in square7)
    elif (6<=row<9 and 3<=col<6):
        check3x3 = (value in square8)
    elif (6<=row<9 and 6<=col<9):
        check3x3 = (value in square9)
    else:
        pass
    
    
    # print(check_row)
    # print(check_col)
    # print(check3x3)
    if (check_row == check_col == check3x3 == False):
        #print(True)
        return True
    else:
        #print(False)
        return False

    
# print(is_valid (board, 0, 0,5)) 
# print(is_valid (board, 0, 2,7)) 
# print(is_valid (board, 0, 2,6)) 
# print(is_valid (board, 3, 5,9)) 

def print_board(board):
    for row in board:
        row_print = ""
        for value in row:
            row_print += (str(value)) + " ";
        print(row_print) 
        #return(row_print)


def solve(board):
    #base case
    slots = find_zeros(board)
    if len(slots) == 0:
        print('Solved!')
        return True
    
    else:
    #recursive case
            r =0
            row = slots[r][0]
            column = slots[r][1]
    for value in range (1,10):
        if is_valid(board, row, column, value) == True:
            board[row][column] = value
            print_board(board)
            print("\n")
            if solve(board):
                return True
            board[row][column] =0                
    return False                 
        
#solve(board)

def main(board):
    print_board(board)
    start_time = time.time()

    solve(board)
    print('--------------------')
    print_board(board)
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main(board)