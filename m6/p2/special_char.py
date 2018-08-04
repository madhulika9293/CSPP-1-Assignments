'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    str_out = ""
    for loop_var in str_input:
        if loop_var in "!@#$%^&*":
            str_out = str_out + " "
        else:
            str_out = str_out + loop_var
    print(str_out)

if __name__ == "__main__":
    main()
