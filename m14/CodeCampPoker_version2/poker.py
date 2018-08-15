'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
# NO_OF_SETS = 1
# NO_OF_CARDS = NO_OF_SETS*52
HAND_SIZE = 5

# MAP_DICT = {'T':10, 'J':11, 'Q':12, 'K':12, 'A':13}

def crd_v(hand):
    excep = {2,3,4,5,14}
    crd_v = set('--23456789TJQKA'.index(c) for c, s in hand)
    if crd_v == excep:
        crd_v.add(1)
        crd_v = crd_v - {14}
    return crd_v

def st_v(hand):
    st_v = set(s for c, s in hand)
    return st_v

    

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    return len(crd_v(hand)) == 5 and (max(crd_v(hand))-min(crd_v(hand)) == 4)

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    return len(st_v(hand)) == 1

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    if is_flush(hand) and is_straight(hand):
        return 3
    if is_flush(hand):
        return 2
    if is_straight(hand):
        return 1
    return 0

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
