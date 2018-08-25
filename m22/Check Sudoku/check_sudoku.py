'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
STR_CHK = '123456789'

def row_check(sudoku):
    '''
    Checks the sudoku rules in each row
    '''
    for each_row in sudoku:
        temp_row = ''.join(sorted(each_row))
        if temp_row != STR_CHK:
            return False
        return True

def col_check(sudoku):
    '''
    Checks the sudoku rules in each row
    '''
    col1 = ''.join(sorted([sudoku[_][0] for _ in range(9)]))
    col2 = ''.join(sorted([sudoku[_][1] for _ in range(9)]))
    col3 = ''.join(sorted([sudoku[_][2] for _ in range(9)]))
    col4 = ''.join(sorted([sudoku[_][3] for _ in range(9)]))
    col5 = ''.join(sorted([sudoku[_][4] for _ in range(9)]))
    col6 = ''.join(sorted([sudoku[_][5] for _ in range(9)]))
    col7 = ''.join(sorted([sudoku[_][6] for _ in range(9)]))
    col8 = ''.join(sorted([sudoku[_][7] for _ in range(9)]))
    col9 = ''.join(sorted([sudoku[_][8] for _ in range(9)]))
    return col1 in STR_CHK and col2 in STR_CHK and col3 in STR_CHK and\
    col4 in STR_CHK and col5 in STR_CHK and col6 in STR_CHK and\
    col7 in STR_CHK and col8 in STR_CHK and col9 in STR_CHK

def grid_check(sudoku):
    '''
    Checks the 3x3 grids in sudoku
    '''
    g_0 = ''.join(sorted([sudoku[i][j] for i in range(0,3) for j in range(0,3)]))
    g_1 = ''.join(sorted([sudoku[i][j] for i in range(0,3) for j in range(3,6)]))
    g_2 = ''.join(sorted([sudoku[i][j] for i in range(0,3) for j in range(6,9)]))
    g_3 = ''.join(sorted([sudoku[i][j] for i in range(3,6) for j in range(0,3)]))
    g_4 = ''.join(sorted([sudoku[i][j] for i in range(3,6) for j in range(3,6)]))
    g_5 = ''.join(sorted([sudoku[i][j] for i in range(3,6) for j in range(6,9)]))
    g_6 = ''.join(sorted([sudoku[i][j] for i in range(6,9) for j in range(0,3)]))
    g_7 = ''.join(sorted([sudoku[i][j] for i in range(6,9) for j in range(3,6)]))
    g_8 = ''.join(sorted([sudoku[i][j] for i in range(6,9) for j in range(6,9)]))
    return g_0 in STR_CHK and g_1 in STR_CHK and g_2 in STR_CHK and\
    g_3 in STR_CHK and g_4 in STR_CHK and g_5 in STR_CHK and\
    g_6 in STR_CHK and g_7 in STR_CHK and g_8 in STR_CHK

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    # print(row_check(sudoku), col_check(sudoku))
    sudoku_int = [int(ele) for row in sudoku for ele in row]
    # print(sudoku_int)
    sum_sud = sum(sudoku_int)
    return sum_sud != 405 and row_check(sudoku) and col_check(sudoku)\
    and grid_check(sudoku)

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for _ in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    sudoku_int = [int(ele) for row in sudoku for ele in row]
    print(check_sudoku(sudoku))
    # print(row_check(sudoku))
    # print(col_check(sudoku))
    # print(grid_check(sudoku))

if __name__ == '__main__':
    main()