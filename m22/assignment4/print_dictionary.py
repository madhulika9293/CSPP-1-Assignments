'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    dict_list = [[] for _ in dictionary]
    for i, each_key in enumerate(dictionary):
        print(i, each_key)
        # dict_list[i][0] = each_key
        # dict_list[i][1] = dictionary[each_key]
    return dict_list

def main():
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
