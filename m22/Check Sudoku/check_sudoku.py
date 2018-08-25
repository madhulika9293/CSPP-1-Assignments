'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
def row_check(sudoku):
    '''
    Checks the sudoku rules in each row
    '''
    for each_row in sudoku:
        temp_row = ''.join(sorted(each_row))
        if temp_row != '123456789':
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
    str_chk = '123456789'
    return (col1 in str_chk and col2 in str_chk and col3 in str_chk and\
    col4 in str_chk and col5 in str_chk and col6 in str_chk and\
    col7 in str_chk and col8 in str_chk and col8 in str_chk)


def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    # print(row_check(sudoku), col_check(sudoku))
    return row_check(sudoku) and col_check(sudoku)

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
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()