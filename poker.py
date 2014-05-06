__author__ = 'anthonylim'

## Anthony Lim
# alim4@ucsc.edu
#
# CMPS 5P, Spring 2014
# Assignment 4
#
# Poker
# ###################
# 23456789TJQKA
# T = 10, J = Jack, Q = Queen, K = King, A = Ace
#
# CDHS
# C = Club, D = Diamond, H = Heart, S = Space
# ####################

import random

def main():
    global deck
    deck = populate_deck()

    ### TESTING ###
    hand = ["JC", "TC", "KC", "QC", "AC"]       # straightflush
    hand2 = ["5C", "5D", "8C", "5S", "5H"]      # fourofakind
    hand3 = ["AH", "AS", "3C", "3H", "AD"]      # fullhouse
    hand4 = ["2H", "TH", "8H", "KH", "5H"]      # flush
    hand5 = ["5C", "9H", "8H", "6D", "7S"]      # straight
    hand6 = ["7C", "9H", "KH", "7D", "7S"]      # threeofakind
    hand7 = ["9C", "JC", "3S", "9D", "JS"]      # twopair
    hand8 = ["TD", "4S", "TH", "2H", "AD"]      # pair
    hand9 = ["TD", "4S", "9H", "2H", "AD"]      # highcard

    #print hand_string(rankpokerhand(hand))
    #print hand_string(rankpokerhand(hand2))
    #print hand_string(rankpokerhand(hand3))
    #print hand_string(rankpokerhand(hand4))
    #print hand_string(rankpokerhand(hand5))
    #print hand_string(rankpokerhand(hand6))
    #print hand_string(rankpokerhand(hand7))
    #print hand_string(rankpokerhand(hand8))
    #print hand_string(rankpokerhand(hand9))

    monte_carlo(10000)

    return

def rankpokerhand(hand):
    if len(hand) != 5:
        print "Error: Hand passed not proper length"
        return

    hmap = build_suit_dict(hand)
    rmap = build_rank_dict(hand)

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

    # **** Straight Flush
    # If 5 of a single suit, straight flush
    if (hmap["club"] or hmap["diamond"] or hmap["heart"] or hmap["spade"]) == 5:
        sf = 0
        for i in range(len(sorted_hand_numeric)-1):
            curr_minus_next = sorted_hand_numeric[i+1] - sorted_hand_numeric[i]
            if curr_minus_next == 1:
                sf += 1
                continue
            else:
                break
        if sf == 4:
            return 1


    # **** Four of a Kind
    # If 4 of a single rank, four of a kind
    for ele in rmap:
        if rmap.get(ele) == 4:
            return 2

    # **** Full House
    for ele in rmap:
        if rmap.get(ele) == 3:
            for i in rmap:
                if rmap.get(i) == 2:
                    return 3

    # **** Flush
    if (hmap["club"] or hmap["diamond"] or hmap["heart"] or hmap["spade"]) == 5:
        return 4

    # **** Straight
    straight = 0
    for i in range(len(sorted_hand_numeric) - 1):
        curr_minus_next = sorted_hand_numeric[i + 1] - sorted_hand_numeric[i]
        if curr_minus_next == 1:
            straight += 1
            continue
        else:
            break
    if straight == 4:
        return 5

    # **** Three of a Kind
    for ele in rmap:
        if rmap.get(ele) == 3:
            # Check if there's not a pair by seeing if there's a 1
            for j in rmap:
                if rmap.get(j) == 1:
                    return 6

    # **** Two Pair && Pair
    pairs = 0
    values = rmap.values()
    for ele in values:
        if ele == 2:
            pairs += 1

    if pairs == 2:
        return 7
    elif pairs == 1:
        return 8

    # **** High Card
    return 9

def build_rank_dict(hand):
    rmap = dict()

    # Initialize from 1 to 9
    for i in range(1, 10):
        rmap["{0}".format(i)] = 0

    rmap["T"] = 0
    rmap["J"] = 0
    rmap["Q"] = 0
    rmap["K"] = 0
    rmap["A"] = 0

    # Count number of each rank in the hand
    for ele in hand:
        if ele[0] == "1":
            rmap["1"] += 1
        if ele[0] == "2":
            rmap["2"] += 1
        if ele[0] == "3":
            rmap["3"] += 1
        if ele[0] == "4":
            rmap["4"] += 1
        if ele[0] == "5":
            rmap["5"] += 1
        if ele[0] == "6":
            rmap["6"] += 1
        if ele[0] == "7":
            rmap["7"] += 1
        if ele[0] == "8":
            rmap["8"] += 1
        if ele[0] == "9":
            rmap["9"] += 1
        if ele[0] == "T":
            rmap["T"] += 1
        if ele[0] == "J":
            rmap["J"] += 1
        if ele[0] == "Q":
            rmap["Q"] += 1
        if ele[0] == "K":
            rmap["K"] += 1
        if ele[0] == "A":
            rmap["A"] += 1

    return rmap

def build_suit_dict(hand):
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

    return hmap

def build_percentages_dict():
    pmap = dict()
    pmap["straightflush"] = 0   # straightflush
    pmap["fourofakind"] = 0     # fourofakind
    pmap["fullhouse"] = 0       # fullhouse
    pmap["flush"] = 0           # flush
    pmap["straight"] = 0        # straight
    pmap["threeofakind"] = 0    # threeofakind
    pmap["twopair"] = 0         # twopair
    pmap["pair"] = 0            # pair
    pmap["highcard"] = 0        # highcard

    return pmap

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
    if rank == 1:
        return "straightflush"
    if rank == 2:
        return "fourofakind"
    if rank == 3:
        return "fullhouse"
    if rank == 4:
        return "flush"
    if rank == 5:
        return "straight"
    if rank == 6:
        return "threeofakind"
    if rank == 7:
        return "twopair"
    if rank == 8:
        return "pair"
    if rank == 9:
        return "highcard"

    print deck[rank]

def monte_carlo(num_hands):
    pmap = build_percentages_dict()
    for i in range(num_hands):
        hand = random.sample(deck, 5)
        pmap[hand_string(rankpokerhand(hand))] += 1

    for ele in pmap:
        print '{0:18s} : {1:.2f}%'.format(ele, (float(pmap.get(ele)) / num_hands)*100)

    return

def populate_deck():
    suit = ['C', 'D', 'H', 'S']
    rank = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    deck = []

    for i in rank:
        for j in suit:
            deck.append(i + j)

    return deck

if __name__ == "__main__":
    main()