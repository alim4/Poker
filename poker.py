__author__ = 'anthonylim'

## Anthony Lim
# alim4@ucsc.edu
#
# CMPS 5P, Spring 2014
# Assignment 3
#
# Poker
# ###################
# 23456789TJQKA
# T = 10, J = Jack, Q = Queen, K = King, A = Ace
#
# CDHS
# C = Club, D = Diamond, H = Heart, S = Space
# ####################


def main():
    deck = populate_deck()
    print deck

    hand = ["2C", "3C", "4C", "5C", "6C"]
    hand2 = ["TC", "JD", "QD", "KD", "AC"]
    hand3 = ["JC", "TC", "KC", "QC", "AC"]

   # rankpokerhand(hand)
    rankpokerhand(hand2)
    #rankpokerhand(hand3)

    return

def rankpokerhand(hand):
    if len(hand) != 5:
        print "Error: Hand passed not proper length"
        return

    hmap = dict()
    hmap["club"] = 0
    hmap["diamond"] = 0
    hmap["heart"] = 0
    hmap["spade"] = 0

    # Count number of each suit in the hand
    for ele in hand:
        if ele[1] == 'C':
            hmap["club"] += 1
        if ele[1] == 'D':
            hmap["diamond"] += 1
        if ele[1] == 'H':
            hmap["heart"] += 1
        if ele[1] == 'S':
            hmap["spade"] += 1

    sorted_hand = []
    sorted_hand_numeric = []

    # Append the rank in the card
    for ele in hand:
        sorted_hand.append(ele[0])

    # Convert that into a number
    for ele in sorted_hand:
        sorted_hand_numeric.append(get_card_order(ele))

    # Sort the hand so that arbitrary orders of hands can be checked
    sorted_hand_numeric.sort()

    # If 5 of a single suit, straight flush
    if (hmap["club"] or hmap["diamond"] or hmap["heart"] or hmap["spade"]) == 5:

        for i in range(len(sorted_hand_numeric)-1):
            if sorted_hand_numeric[i+1] - sorted_hand_numeric[i] == 1:
                continue
            else:
                break

        print "straightflush"
        return 1

    # If 4 of a single suit, four of a kind
    if (hmap["club"] or hmap["diamond"] or hmap["heart"] or hmap["spade"]) == 4:
        print "fourofakind"
        #return 2

    # Full House
    for ele in hmap:
        if hmap.get(ele) == 3:
            for i in hmap:
                if hmap.get(i) == 2:
                    # return 3
                    print "fullhouse"

    # Straight

    return

def get_card_order(val):
    if val == "1":
        return 1
    if val == "2":
        return 2
    if val == "3":
        return 3
    if val == "4":
        return 4
    if val == "5":
        return 5
    if val == "6":
        return 6
    if val == "7":
        return 7
    if val == "8":
        return 8
    if val == "9":
        return 9
    if val == "T":
        return 10
    if val == "J":
        return 11
    if val == "Q":
        return 12
    if val == "K":
        return 13
    if val == "A":
        return 14

def hand_string(rank):
    return

def monte_carlo(num_hands):
    return

def populate_deck():
    suit = ['C', 'D', 'H', 'S']
    rank = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    deck = []

    for i in rank:
        for j in suit:
            deck.append(i + j)

    return deck


main()