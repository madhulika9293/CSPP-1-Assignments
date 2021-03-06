'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math

def clean(inp):
    '''
        Make a words list and clean up the words
    '''
    regex = re.compile('[^a-z]') # cap means only
    return [regex.sub('', word.strip()) for word in inp.lower().split(' ')]

def word_freq(list_of_words, index, dictionary=None):
    '''
    Words frequency calculator
    '''
    stop_words = load_stopwords('stopwords.txt')
    for word in list_of_words:
        if word != "" and word not in stop_words:
            if word not in dictionary:
                dictionary[word] = [0, 0]
            dictionary[word][index] += 1
    return dictionary

def computation(dictionary):
    '''
    necessary computation
    '''
    num = sum(value[0]*value[1] for value in dictionary.values())
    den1 = math.sqrt(sum(value[0]**2 for value in dictionary.values()))
    den2 = math.sqrt(sum(value[1]**2 for value in dictionary.values()))
    return num/(den1*den2)

def similarity(input1, input2):
    '''
        Compute the document distance as given in the PDF
    '''
    input1 = clean(input1)
    input2 = clean(input2)

    dictionary = {}
    dictionary = word_freq(input1, 0, {})
    dictionary = word_freq(input2, 1, dictionary)

    return computation(dictionary)

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as file:
        for line in file:
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
