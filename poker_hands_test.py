from cards import Card
from poker_calc import hand_ranker
#probably import something from poker_calc here!

def calc_score(hand):
    # Call your code from poker_calc here!
    return hand_ranker(hand)

def test_hands():
    HAND_VALUES = {"four_kind": 25, "fullhouse": 9, "flush": 6, "straight": 4, "three": 3, "two_pair":2, "jacks_pair": 1}
    
    testHand_four = [Card(5, 'Spades'), Card(5, 'Hearts'),  Card(5, 'Clubs'),  Card(5, 'Diamonds'),  Card(3, 'Hearts')]
    testHand_fullhouse = [Card(12, 'Spades'), Card(11, 'Diamonds'),  Card(11, 'Spades'),  Card(12, 'Diamonds'),  Card(12, 'Clubs')]
    testHand_flush = [Card(5, 'Spades'), Card(6, 'Spades'),  Card(2, 'Spades'),  Card(10, 'Spades'),  Card(11, 'Spades')]
    testHand_straight = [Card(1, 'Spades'), Card(12, 'Spades'),  Card(13, 'Diamonds'),  Card(10, 'Diamonds'),  Card(11, 'Spades')]
    testHand_three = [Card(5, 'Spades'), Card(7, 'Hearts'),  Card(5, 'Clubs'),  Card(5, 'Diamonds'),  Card(3, 'Hearts')]
    testHand_two_pair = [Card(5, 'Spades'), Card(7, 'Hearts'),  Card(7, 'Clubs'),  Card(5, 'Diamonds'),  Card(3, 'Hearts')]
    testHand_jack_pair = [Card(13, 'Spades'), Card(13, 'Hearts'),  Card(7, 'Clubs'),  Card(5, 'Diamonds'),  Card(3, 'Hearts')]
    testHand_jack_pair2 = [Card(1, 'Spades'), Card(1, 'Hearts'),  Card(7, 'Clubs'),  Card(5, 'Diamonds'),  Card(3, 'Hearts')]
    testHand_bad1 = [Card(10, 'Spades'), Card(11, 'Hearts'),  Card(7, 'Clubs'),  Card(5, 'Diamonds'),  Card(3, 'Diamonds')]
    testHand_bad2 = [Card(10, 'Spades'), Card(10, 'Hearts'),  Card(7, 'Clubs'),  Card(5, 'Diamonds'),  Card(3, 'Diamonds')]
    testHand_bad3 = [Card(2, 'Spades'), Card(3, 'Hearts'),  Card(7, 'Clubs'),  Card(5, 'Diamonds'),  Card(3, 'Diamonds')]
    testHand_bad4 = [Card(1, 'Spades'), Card(2, 'Spades'),  Card(3, 'Diamonds'),  Card(4, 'Diamonds'),  Card(5, 'Spades')]

    print("Testing hands...")
    assert calc_score(testHand_four) == HAND_VALUES["four_kind"]
    assert calc_score(testHand_fullhouse) == HAND_VALUES["fullhouse"]
    assert calc_score(testHand_flush) == HAND_VALUES["flush"]
    assert calc_score(testHand_straight) == HAND_VALUES["straight"]
    assert calc_score(testHand_three) == HAND_VALUES["three"]
    assert calc_score(testHand_two_pair) == HAND_VALUES["two_pair"]
    assert calc_score(testHand_jack_pair) == HAND_VALUES["jacks_pair"]
    assert calc_score(testHand_jack_pair2) == HAND_VALUES["jacks_pair"]
    assert calc_score(testHand_bad1) == 0
    assert calc_score(testHand_bad2) == 0       # Pair is too low
    assert calc_score(testHand_bad3) == 0
    assert calc_score(testHand_bad4) == 0       # Aces only count as high
    print("Successful on the test hands.")
    
if __name__ == "__main__":
    test_hands()
