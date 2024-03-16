from dataclasses import dataclass
from collections import Counter


@dataclass
class Hand:
    hand: list[int]
    bid: int

    @classmethod
    def create(cls, line: str):
        hand_str, bid = line.strip().split()
        bid = int(bid)
        hand = []
        # Replace A, K, Q, J, T for [14, 13, 12, 0, 10]
        for char in hand_str:
            if char == "A":
                hand.append(14)
            elif char == "K":
                hand.append(13)
            elif char == "Q":
                hand.append(12)
            elif char == "J":
                hand.append(0)
            elif char == "T":
                hand.append(10)
            else:
                hand.append(int(char))
        return cls(hand, bid)

    def __eq__(self, other):
        return self.hand == other.hand

    def __ne__(self, other):
        return self.hand != other.hand

    def __lt__(self, other):
        if self.type < other.type:
            return True
        if self.type > other.type:
            return False
        return self.hand < other.hand

    def __gt__(self, other):
        if not (self < other) and self != other:
            return True
        return False

    @property
    def type(self):
        """Find the type of the hand and give them a number"""
        if not hasattr(self, "_type"):
            # Looking for how many identical cards are in the hand
            counts_card = Counter(self.hand)
            # IF J/0 are in the hand replace it make the hand the strongest type possible
            if 0 in counts_card.keys() and len(counts_card) != 1:
                n_j = counts_card.pop(0)
                max_card = sorted(
                    counts_card.items(), key=lambda item: item[1], reverse=True
                )[0][0]
                counts_card[max_card] += n_j

            counts_card = list(counts_card.values())
            counts_card.sort(reverse=True)

            # Evaluate the types
            # 5 of a kind for 7
            if counts_card == [5]:
                self._type = 7
            # 4 of a kind for 6
            elif counts_card == [4, 1]:
                self._type = 6
            # Full house for 5
            elif counts_card == [3, 2]:
                self._type = 5
            # 3 of a kind for 4
            elif counts_card == [3, 1, 1]:
                self._type = 4
            # 2 pair for 3
            elif counts_card == [2, 2, 1]:
                self._type = 3
            # 1 pair for 2
            elif counts_card == [2, 1, 1, 1]:
                self._type = 2
            elif counts_card == [1, 1, 1, 1, 1]:
                # All different for 1
                self._type = 1
            else:
                raise ValueError(f"Invalid card {self}", counts_card)
        return self._type


def read_input(fname):
    with open(fname) as file:
        hands = [Hand.create(line) for line in file]
    return hands


def first_part(hands):
    hands.sort()
    return sum([hand.bid * (i + 1) for i, hand in enumerate(hands)])


if __name__ == "__main__":
    # Read input file
    # fname = "exp-data.txt"
    fname = "input.txt"
    hands = read_input(fname)
    result = first_part(hands)
    print("The total winnings is: ", result)
    # result2 = second_part(times, distances_race)
    # print("The  multiplication of the number of way to win is: ", result2)
