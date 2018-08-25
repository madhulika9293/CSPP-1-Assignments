'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    freq_dict = {}
    lst_inp = string.split(" ")
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
