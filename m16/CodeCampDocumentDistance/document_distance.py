'''
    Document Distance - A detailed description is given in the PDF
'''
import math

def word_dict(inp):
    '''
        Make a words list and clean up the words
    '''
    stop_words = load_stopwords('stopwords.txt')
    inp = inp.lower()
    for char in inp:
        if char in '!~@#$%^&*.3?':
            inp = inp.replace(char, '')
    inp = inp.strip().split(" ")
    i_1 = {}
    # write condition for stop words
    for val in inp:
        if val not in stop_words and val != "":
            if val in i_1:
                i_1[val] += 1
            else:
                i_1[val] = 1
    return i_1


def similarity(input1, input2):
    '''
        Compute the document distance as given in the PDF
    '''
    dict_inp1 = word_dict(input1)
    dict_inp2 = word_dict(input2)

    com_dict = {}
    com_words = set(list(dict_inp1.keys()) + list(dict_inp2.keys()))

    for loop_var in com_words:
        if loop_var in dict_inp1 and loop_var in dict_inp2:
            com_dict[loop_var] = [dict_inp1[loop_var], dict_inp2[loop_var]]
        elif loop_var in dict_inp1 and loop_var not in dict_inp2:
            com_dict[loop_var] = [dict_inp1[loop_var], 0]
        elif loop_var not in dict_inp1 and loop_var in dict_inp2:
            com_dict[loop_var] = [0, dict_inp2[loop_var]]

    sim_num = sum([com_dict[word][0]*com_dict[word][1] for word in com_dict])
    sim_den1 = math.sqrt(sum([com_dict[word][0]**2 for word in com_dict]))
    sim_den2 = math.sqrt(sum([com_dict[word][1]**2 for word in com_dict]))

    # print(com_dict)
    # print(sim_num, sim_den1, sim_den2)

    cos_dist = sim_num/(sim_den1*sim_den2)

    return cos_dist

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
