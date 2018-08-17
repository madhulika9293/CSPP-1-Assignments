'''
    Document Distance - A detailed description is given in the PDF
'''
def word_list(inp1):
    inp1.lower()
    for char in inp1:
        if char in '!~@#$%^&*.':
            inp1 = inp1.replace(char, '')
    inp1.strip()
    i_1 = inp1.split(" ")
    return i_1

def similarity(dict1, dict2):
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
    stop_file = stopwords.txt
    print(load_stopwords(stop_file))
    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
