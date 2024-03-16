from dataclasses import dataclass


@dataclass
class Card:
    """Class"""

    ids: int
    win_values: list
    values: list

    def coincidences(self):
        """Return the number of coincidence between the winning values
        and the card values"""
        coin = 0
        for value in self.values:
            if value in self.win_values:
                coin += 1
        return coin


def read_input(fname):
    """Return a list of Card"""
    cards_list = []
    with open(fname) as data:
        for line in data:
            win_card, card = line.strip().split("|")
            card_id, win_card = win_card.split(":")
            card_id = int(card_id.split()[1])
            win_card = [int(ele) for ele in win_card.split()]
            card = [int(ele) for ele in card.split()]
            cards_list.append(Card(card_id, win_card, card))
    return cards_list


def first_part(cards_list):
    """Return the total of points from a list of cards"""
    winning = []
    for card in cards_list:
        winning.append(int(2 ** (card.coincidences() - 1)))
    return sum(winning)


def second_part(cards_list):
    """Return the number of copies made from a list of cards"""
    number_copies = [0 for i in range(len(cards_list))]
    for nc, card in enumerate(cards_list):
        for coin in range(card.coincidences()):
            number_copies[nc + 1 + coin] += 1 + number_copies[nc]
    return sum(number_copies) + len(cards_list)


if __name__ == "__main__":
    # Read input file
    # fname = "exp-data.txt"
    fname = "input.txt"
    cards_list = read_input(fname)
    points = first_part(cards_list)
    print("The total points is: ", points)
    total_copies = second_part(cards_list)
    print("Total of scratchcards: ", total_copies)
