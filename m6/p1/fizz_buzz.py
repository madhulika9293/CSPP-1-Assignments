'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
    num = int(input())
    for loop_var in range(1, num+1):
        if loop_var%3 == 0:
            print("Fizz")
        if loop_var%5 == 0:
            print("Buzz")
        if loop_var%3 != 0 and loop_var%5 != 0:
            print(str(loop_var))

if __name__ == "__main__":
    main()
