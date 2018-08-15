'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
import collections

# NO_OF_SETS = 1
# NO_OF_CARDS = NO_OF_SETS*52

def crd_v(hand):
    '''calculates card values'''
    excep = [2, 3, 4, 5, 14]
    crd_val = ['--23456789TJQKA'.index(c) for c, s in hand]
    if crd_val == excep:
        crd_val.remove(14)
        crd_val.add(1)
    return crd_val

def st_v(hand):
    '''calculates suit values'''
    st_val = [s for c, s in hand]
    return st_val

def is_straight(hand):
    ''' Straight hand function '''
    return len(crd_v(hand)) == 5 and (max(crd_v(hand))-min(crd_v(hand)) == 4)

def is_flush(hand):
    ''' flush hand function '''
    return len(set(st_v(hand))) == 1

def is_four_of_a_kind(hand):
    ''' Four of a kind hand function '''
    return list(collections.Counter(crd_v(hand)).values()) == [4, 1]

def is_fullhouse(hand):
    ''' Full House hand function '''
    return sorted(list(collections.Counter(crd_v(hand)).values())) == [2, 3]

def is_three_of_kind(hand):
    ''' Three of kind hand function '''
    return sorted(list(collections.Counter(crd_v(hand)).values())) == [1, 1, 3]

def is_twopair(hand):
    ''' Three of kind hand function '''
    return sorted(list(collections.Counter(crd_v(hand)).values())) == [1, 2, 2]

def is_onepair(hand):
    ''' Three of kind hand function '''
    return sorted(list(collections.Counter(crd_v(hand)).values())) == [1, 1, 1, 2]

def hand_rank(hand):
    ''' ranks the card '''
    if is_flush(hand) and is_straight(hand):
        return 1
    if is_four_of_a_kind(hand):
        return 2
    if is_fullhouse(hand):
        return 3
    if is_flush(hand):
        return 4
    if is_straight(hand):
        return 5
    if is_three_of_kind(hand):
        return 6
    if is_twopair(hand):
        return 7
    if is_onepair(hand):
        return 8
    return 9


def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''
    return min(hands, key=hand_rank)

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
