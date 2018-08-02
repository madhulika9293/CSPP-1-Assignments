"""A program that prints the longest substring of s
in which the letters occur in alphabetical order"""

def main():
    str_inp = input()
    str_inp = str(input("Enter input string: "))
    count_out = 0
    check_inp = 0
    pos_out = 0
    index_out = 0
    for I in range(len(str_inp)-1):
        if ord(str_inp[I]) <= ord(str_inp[I+1]):
            check_inp += 1
        else:
            check_inp = 0
        if check_inp > count_out:
            count_out = check_inp
            index_out = I
    pos_out = index_out+1-count_out
    print("Longest substring in alphabetical order is: " + str_inp[pos_out:pos_out+count_out+1])

if __name__== "__main__":
    main()
