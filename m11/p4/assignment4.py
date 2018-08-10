'''
Exercise: Assignment-4
We are now ready to begin writing the code that interacts
with the player. We'll be implementing the playHand function.
This function allows the user to play out a single hand.
First, though, you'll need to implement the helper calculateHandlen function,
which can be done in under five lines of code.
'''

def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    sum = 0
    for key_dict in hand:
        sum += hand[key_dict]
    return sum


def main():
    n=input()
    adict={}
    for i in range(int(n)):
        data=input()
        l=data.split()
        adict[l[0]]=int(l[1])
    print(calculate_handlen(adict))
        


if __name__== "__main__":
    main()