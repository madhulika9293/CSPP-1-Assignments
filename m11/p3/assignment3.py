# Assignment-3
'''
Fill in the code for isValidWord in ps4a.py and be sure
you've passed the appropriate tests in test_ps4a.py before
pasting your function definition here.
'''

def is_validword(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    count = 0
    for char in word:
        if char in hand:
            count += 1
    if count == len(word):
        if word in word_list:
            return True
    return False

def main():
    '''
    Main function
    '''
    word = input()
    num_inp = int(input())
    adict = {}
    for _ in range(num_inp):
        data = input()
        l_inp = data.split()
        adict[l_inp[0]] = int(l_inp[1])
    l2_inp = input().split()
    print(is_validword(word, adict, l2_inp))

if __name__ == "__main__":
    main()
