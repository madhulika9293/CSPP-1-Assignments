"""A python program to find the square root of the given
number using approximation method"""

def main():
    """This is the code for M5-A3"""
    str_inp = input()
    epsilon = 0.01
    low_inp = 1.0
    high_inp = str_inp
    sq_root = (high_inp + low_inp)/2.0
    while abs(sq_root**2 - str_inp) >= epsilon:
        if sq_root**2 < str_inp:
            low_inp = sq_root
        else:
            high_inp = sq_root
        sq_root = (high_inp + low_inp)/2.0
    if abs(sq_root**2 - str_inp) <= epsilon:
        print(str(sq_root))
if __name__ == "__main__":
    main()
