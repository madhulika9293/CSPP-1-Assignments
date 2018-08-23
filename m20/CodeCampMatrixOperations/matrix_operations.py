def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(m1[0]) != len(m2):
       print("Error: Matrix shapes invalid for mult")
       return None
    rows_out = len(m1)
    col_out = len(m2[0])
    iter_out = len(m2)
    mat_mult = [[] for i in range(rows_out)]
    for i in range(rows_out):
        for j in range(col_out):
            temp = 0
            for k in range(iter_out):
                temp += m1[i][k]*m2[k][j]
            mat_mult[i] += [temp]
    return mat_mult[:] 

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(m1) != len(m2):
        print("Error: Matrix shapes invalid for addition")
        return None
    elif len(m1[0]) != len(m2[0]):
        print("Error: Matrix shapes invalid for addition")
        return None
    else:
        mat_add = [[0 for j in range(len(m1[0]))] for i in range(len(m1))]
        for i,mat in enumerate(m1):
            for j, _ in enumerate(mat):
                mat_add[i][j] = int(m1[i][j]) + int(m2[i][j])
    return mat_add[:]

def read_matrix(mat_inp):
    '''
    rows = int(input())
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix = []
    for i in range(int(mat_inp[0])):
        matrix += [[int(var) for var in input().split(" ")]]
        if len(matrix[i]) != int(mat_inp[1]):
            print("Error: Invalid input for the matrix")
            return None
    return matrix

def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2

    mat_inp_1 = input().split(",")
    mat_1 = read_matrix(mat_inp_1)

    mat_inp_2 = input().split(",")
    mat_2 = read_matrix(mat_inp_2)

    # print(mat_1) 
    # print(mat_2) 
    print(add_matrix(mat_1, mat_2))
    print(mult_matrix(mat_1, mat_2))

if __name__ == '__main__':
    main()
