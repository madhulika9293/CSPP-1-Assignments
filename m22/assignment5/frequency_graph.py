'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    dict_list = []
    for each_key in dictionary:
        dict_list.append([each_key, dictionary[each_key]])
    dict_list = sorted(dict_list)
    for each_ele in dict_list:
        print(each_ele[0], "-", str('#'*each_ele[1]))

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
