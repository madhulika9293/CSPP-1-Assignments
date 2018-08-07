'''
Python program to calculate factorial of a given integer using recursion
'''

def factorial(n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if n <= 1:
        return 1
    return n*factorial(n-1)


def main():
    a = int(input())
    print(factorial(int(a)))    

if __name__== "__main__":
    main()
