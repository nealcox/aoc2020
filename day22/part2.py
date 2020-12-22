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
    cards, winner = combat(cards, 1)
    winning_cards = cards[winner]

    print(f"Winning cards: {winning_cards}")
    score = 0
    num_cards = len(winning_cards)
    for m in range(num_cards, 0, -1):
        score += m * winning_cards[num_cards - m]
    return score


def combat(cards, game_no):
    turns = 0
    finished = False
    seen = set()
    while not finished:
        turns += 1
        # print(f"Before round {turns} (Game {game_no}):\nPlayer 1 {cards[0]}\nPlayer 2 {cards[1]}")
        config = (tuple(cards[0]), tuple(cards[1]))
        if config in seen:  # If previous game state, player 1 wins
            finished = True
            winner = 0
            loser = 1
        elif len(cards[0]) == 0:  # If a player runs outof cards: loses
            finished = True
            winner = 1
            loser = 0
        elif len(cards[1]) == 0:
            finished = True
            winner = 0
            loser = 1

        else:  # Can play a normal round
            cards_turn = []
            for i, player_cards in enumerate(cards):
                cards_turn.append(player_cards.pop(0))
            # Play recursive game if both players have enough cards
            if (len(cards[0]) >= cards_turn[0]) and (len(cards[1]) >= cards_turn[1]):
                recurse_cards = [cards[0][: cards_turn[0]], cards[1][: cards_turn[1]]]
                _, winner = combat(recurse_cards, game_no + 1)
                if winner == 1:
                    loser = 0
                else:
                    loser = 1

            else:  # can't recurse: higher card wins
                if cards_turn[0] > cards_turn[1]:
                    winner = 0
                    loser = 1
                elif cards_turn[1] > cards_turn[0]:
                    winner = 1
                    loser = 0
            # Add cards played in the turn to the winners cards
            cards[winner].append(cards_turn[winner])
            cards[winner].append(cards_turn[loser])
        seen.add(config)
        # print(f"After round {turns} (Game {game_no}):\nPlayer 1 {cards[0]}\nPlayer 2 {cards[1]}")
        if not cards[0]:
            finished = True
            winner = 1
        elif not cards[1]:
            finished = True
            winner = 0

    return cards, winner


if __name__ == "__main__":
    exit(main())
