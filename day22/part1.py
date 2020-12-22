import re
import sys
from collections import defaultdict
from itertools import permutations


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "input.txt"
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    answer = None
    players_details = input_text.strip().split("\n\n")

    cards = []
    for player in players_details:
        name, cards_s = player.split(":\n")
        player_cards = [int(c) for c in cards_s.strip().split("\n")]
        cards.append(player_cards)
    print(cards)

    turns = 0
    finished = False
    while not finished:
        cards_turn = []
        for i, player_cards in enumerate(cards):
            cards_turn.append(player_cards.pop(0))
        if cards_turn[0] > cards_turn[1]:
            cards[0].append(cards_turn[0])
            cards[0].append(cards_turn[1])
        elif cards_turn[1] > cards_turn[0]:
            cards[1].append(cards_turn[1])
            cards[1].append(cards_turn[0])
        else:
            raise ValueError("Draw! {cards_turn}")
        turns += 1
        print(f"Round {turns}:\nPlayer 1 {cards[0]}\nPlayer 2 {cards[1]}")
        if not (cards[0] and cards[1]):
            finished = True

        winning_cards = cards[0] + cards[1]
        print(f"Winning cards: {winning_cards}")
        score = 0
        num_cards = len(winning_cards)
        for m in range(num_cards, 0, -1):
            score += m * winning_cards[num_cards - m]
    return score


if __name__ == "__main__":
    exit(main())
