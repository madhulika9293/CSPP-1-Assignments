'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re

def tokenize(string):
    freq_dict = {}
    regex = re.compile("[^a-zA-Z0-9 ]")
    string_mod = regex.sub('', string)
    lst_inp = string_mod.split(" ")[:-1]
    for each_word in lst_inp:
        if each_word not in freq_dict:
            freq_dict[each_word] = lst_inp.count(each_word)
    return freq_dict
    
            
def main():
    num_lines = int(input())
    string_inp = ''
    for _ in range(num_lines):
        string_inp += input()
        string_inp += " "
    print(tokenize(string_inp))

if __name__ == '__main__':
    main()
