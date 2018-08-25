'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    num_lines = int(input())
    for _ in range(num_lines):
    	str = input()
    	print(str)

if __name__ == '__main__':
    main()
