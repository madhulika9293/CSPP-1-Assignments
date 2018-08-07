'''
Python program to calculate factorial of a given integer using recursion
'''

def factorial(num_inp):
    '''
    num_inp is positive Integer

    returns: a positive integer, the factorial of num_inp.
    '''
    if num_inp <= 1:
        return 1
    return num_inp*factorial(num_inp-1)


def main():
    '''
    Main function to upon the declared function
    '''
    num_out = int(input())
    print(factorial(int(num_out)))    

if __name__ == "__main__":
    main()
