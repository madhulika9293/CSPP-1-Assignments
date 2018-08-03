"""A python program to find the square root of the given number
using approximation method"""

def main():
    """This is the code for M5-A2"""
    str_inp = float(input())
    epsi_inp = 0.01
    guess_inp = 0.00
    incr_inp = 0.1
    while abs(guess_inp**2 - str_inp) >= epsi_inp and guess_inp <= str_inp:
        guess_inp += incr_inp
    if abs(guess_inp**2 - str_inp) >= epsi_inp:
        print("Failed")
    else:
        print(str(guess_inp))
if __name__ == "__main__":
    main()
