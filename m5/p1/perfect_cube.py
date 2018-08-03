"""Write a python program to find if the given number is a perfect cube or not
using guess and check algorithm"""

def main():
    """This is the code for M5-A1"""
    str_inp = int(input())
    guess_inp = 0.0
    for loop_var in range(str_inp):
        if loop_var**3 == str_inp:
            guess_inp = loop_var
            break
    if abs(guess_inp**3 - str_inp) == 0:
        print(str(str_inp) + " is a perfect cube")
    else:
        print(str(str_inp) + " is not a perfect cube")
if __name__ == "__main__":
    main()
