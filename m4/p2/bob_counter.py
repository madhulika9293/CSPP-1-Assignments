"""A program that prints the number of times the
string 'bob' occurs in s"""
def main():
    """ This is the code for M4-A2"""
    str_inp = input()
    cnt_inp = 0
    for ind_inp in range(len(str_inp)-1):
        if len(str_inp[ind_inp:ind_inp+3]) == 3 and str_inp[ind_inp:ind_inp+3] in 'bob':
            cnt_inp += 1
    print('Number of times bob occurs is: ' + str(cnt_inp))

if __name__ == "__main__":
    main()
