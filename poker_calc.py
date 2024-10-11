"""
Author: Evan and Connor
File: poker_gui.py
Project 11
Module for calculating the value of a given poker hand
"""
from cards import Card

HAND_VALUES = {"four_kind": 25, "fullhouse": 9, "flush": 6, "straight": 4, "three": 3, "two_pair":2, "jacks_pair": 1}

def hand_ranker(deck):
    cards = []
    for card in deck:
        cards.append(card.rank)
    for x in range(1,14):
        if cards.count(x) == 4:
            #print("four_kind")
            return HAND_VALUES["four_kind"]
    for x in range(1,14):
        if cards.count(x) == 3:
            for y in range(1,14):
                if x != y:
                    if cards.count(y) == 2:
                        #print("fullhouse")
                        return HAND_VALUES["fullhouse"]
            #print("three")
            return HAND_VALUES["three"]
    for x in range(1,14):
        if cards.count(x) == 2:
            for y in range(1,14):
                if x != y:
                    if cards.count(y) == 2:
                        #print("two_pair")
                        return HAND_VALUES["two_pair"]
            if x == 1 or x > 10:
                #print("jacks_pair")
                return HAND_VALUES["jacks_pair"]
    if deck[0].suit == deck[1].suit and deck[1].suit == deck[2].suit and deck[2].suit == deck[3].suit and deck[3].suit == deck[4].suit:
        #print("flush")
        return HAND_VALUES["flush"]    
    
    cards.sort()
    if cards.count(1) > 0:
        cards.remove(1)
        cards.append(14)
    if cards[0] == cards[1] - 1 and cards[0] == cards[2] - 2 and cards[0] == cards[3] - 3 and cards[0] == cards[4] - 4:
        #print("straight")
        return HAND_VALUES["straight"]

            
    
    
    #print(0)
    return 0

        

    #print(cards)







