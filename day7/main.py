from dataclasses import dataclass

@dataclass
class CamelCardsRound:
    hand: str
    bid: int
    score: int = 0


# card labels from worst to best
card_labels = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def cal_hand_score(hand: str):
    cards = [c for c in hand]
    card_count = count_cards(cards)
    rank = cal_hand_rank(card_count)

    rank_repr = str(rank)
    for i in range(len(cards)):
        rank_repr += str(card_labels.index(cards[i])).zfill(2)
            

    return int(rank_repr)

# hand rankings, from best to worst
# 7: five of a kind 
# 6: four of a kind
# 5: full house
# 4: three of a kind
# 3: two pair
# 2: one pair
# 1: high card

def cal_hand_rank(card_count: dict):
    hand_repr = ''
    card_count = dict(sorted(card_count.items(), key=lambda item: item[1], reverse=True))
    for c in card_count.values(): hand_repr += str(c)

    match hand_repr:
        case '5':
            # print('five of a kind')
            return 7
        case '41':
            # print('four of a kind')
            return 6
        case '32':
            # print('full house')
            return 5
        case '311':
            # print('three of a kind')
            return 4
        case '221':
            # print('two pair')
            return 3
        case '2111':
            # print('one pair')
            return 2
        case _:
            # print('high card')
            return 1


def count_cards(cards: list):
    count = {}
    for card in cards:
        if card in count:
            count[card] += 1
        else:
            count[card] = 1

    return count

# general text file reading to list of rounds
text_file = open('input.txt','r')
lines = text_file.readlines()
lines = [line.strip() for line in lines]
text_file.close()

rounds = []
for line in lines:
    hand, bid = line.split(' ')
    rounds.append(CamelCardsRound(hand, int(bid)))

# part 1

for round in rounds:
    round.score = cal_hand_score(round.hand)

rounds.sort(key=lambda r: r.score)

sum_winnings = 0;
for i in range(len(rounds)):
    round = rounds[i]
    print(f'{i + 1}: {round.hand} {round.bid} * {i+1} = {round.bid * (i + 1)} ({round.score})')
    sum_winnings += round.bid * (i + 1)

print("part 1", sum_winnings)