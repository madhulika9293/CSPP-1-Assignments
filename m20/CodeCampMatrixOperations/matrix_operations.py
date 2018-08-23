def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    pass

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    pass

def read_matrix():
    '''
    rows = int(input())
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    mat_rows_columns = (input(), input()) 
    # mat_columns = int(input())
    matrix = []
    for i in range(mat_rows_columns[0]):
        matrix += [input()]
        if len(matrix[i]) != mat_rows_columns[1]:
            print("Error: Invalid input for the matrix")
            return None
    return matrix

def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2

    mat_1 = read_matrix()
    # mat_2 = read_matrix()
    print(mat_1) 
    # print(mat_2) 

if __name__ == '__main__':
    main()
