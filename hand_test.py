from pytest import approx
from hand import Hand


def testOneAce():
    hand = Hand()
    hand.setter(10, 1)
    assert(hand.getTotalPoints() == 21)


def testTwoAce():
    hand = Hand()
    hand.setter(5, 2)
    assert(hand.getTotalPoints() == 17)


def testThreeAce():
    hand = Hand()
    hand.setter(1, 3)
    assert(hand.getTotalPoints() == 14)



def testNormal():
    hand = Hand()
    hand.setter(15, 0)
    assert(hand.getTotalPoints() == 15)


def testWin():
    hand = Hand()
    hand.setter(20, 1)
    assert(hand.getTotalPoints() == 21)


def testOver():
    hand = Hand()
    hand.setter(21, 1)
    assert(hand.getTotalPoints() == 22)

