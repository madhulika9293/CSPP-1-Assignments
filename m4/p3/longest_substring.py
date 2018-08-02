"""A program that prints the longest substring of s
in which the letters occur in alphabetical order"""

def main():
    """ This is the code for M4-A1"""
    str_inp = input()
    count_out = 0
    check_inp = 0
    pos_out = 0
    index_out = 0
    for loop_var in range(len(str_inp)-1):
        if ord(str_inp[loop_var]) <= ord(str_inp[loop_var+1]):
            check_inp += 1
        else:
            check_inp = 0
        if check_inp > count_out:
            count_out = check_inp
            index_out = loop_var
    pos_out = index_out+1-count_out
    print(str_inp[pos_out:pos_out+count_out+1])

if __name__ == "__main__":
    main()
