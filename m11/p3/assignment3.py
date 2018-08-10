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
    word = input()
    n = int(input())
    adict = {}
    for i in range(n):
        data = input()
        l = data.split()
        adict[l[0]] = int(l[1])
    l2 = input().split()
    print(is_validword(word, adict, l2))

if __name__ == "__main__":
    main()
