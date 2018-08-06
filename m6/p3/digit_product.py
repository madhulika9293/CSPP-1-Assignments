'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    if int_input == 0:
        print(str(0))
    else:
        prod_out = 1
        nf_flag = 0
        if int_input < 0:
            nf_flag = -1
            int_input = int_input*-1
        while int_input > 0:
            prod_out = prod_out*(int_input%10)
            int_input = int_input//10
        print(prod_out*nf_flag)

if __name__ == "__main__":
    main()
