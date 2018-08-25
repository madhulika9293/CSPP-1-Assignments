'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''
    This is a function to print given input
    '''
    num_lines = int(input())
    for _ in range(num_lines):
        str_inp = input()
        print(str_inp)

if __name__ == '__main__':
    main()
