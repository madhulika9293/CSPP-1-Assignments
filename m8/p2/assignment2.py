'''
a Python function, sumofdigits, that takes in one number and
returns the sum of digits
of given number.
'''

def sumofdigits(n_inp):
    '''
    n_inp is positive Integer

    returns: a positive integer, the sum of digits of n_inp.
    '''
    if n_inp == 0:
        return 0
    return n_inp%10 + sumofdigits(n_inp//10)
def main():
    '''
    this is the main function
    '''
    num_op = input()
    print(sumofdigits(int(num_op)))  

if __name__ == "__main__":
    main()
