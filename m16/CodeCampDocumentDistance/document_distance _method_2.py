'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math

def word_dict(inp):
    '''
        Make a words list and clean up the words
    '''
    inp = inp.lower()
    regex = re.compile('[^a-z]') # cap means only
    inp = regex.sub('',inp)
    list_of_words = inp.split()
    for word_index in enumerate(inp):
        list_of_words[word_index] = list_of_words[word_index].strip()
    return list_of_words

def rem_stp_wrds(list_of_words):
    stop_words = load_stopwords('stopwords.txt')
    for word in list_of_words:
        if word in stop_words:
            list_of_words.remove(word)
    return list_of_words

def word_freq(list_of_words, index, dictionary = {})
    for word in list_of_words:
        if word != "":
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
    

def similarity(input1, input2):
    '''
        Compute the document distance as given in the PDF
    '''
    

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
    print(word_dict(input1))

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
