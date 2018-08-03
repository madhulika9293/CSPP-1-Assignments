"""A python program to find the square root of the given number
using Newton-Raphson Method"""
def main():
    """This is the code for M4-A4"""
    epsilon = 0.01
    str_inp = float(input())
    sq_rt = str_inp/2.0
    while abs(sq_rt*sq_rt - str_inp) >= epsilon:
        sq_rt = sq_rt - (((sq_rt**2) - str_inp)/(2*sq_rt))
    print(str(sq_rt))
if __name__ == "__main__":
    main()
