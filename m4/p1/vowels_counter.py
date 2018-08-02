"""To write a program that counts up the number of vowels
contained in the string s"""

def main():
    """ This is the code for M4-A1"""
    str_inp = raw_input()
    cnt_inp = 0
    for i in str_inp:
        if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            cnt_inp += 1
    print("Number of vowels: " + str(cnt_inp))

if __name__ == "__main__":
    main()
