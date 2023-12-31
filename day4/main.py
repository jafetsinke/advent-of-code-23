text_file = open('input.txt','r')
lines = text_file.readlines()
text_file.close()

def parse_digits_str(digits_str: str):
    digits = []
    for char in digits_str.split(" "):
        if char.isdigit():
            digits.append(int(char))
    return digits

def compare_digits(valid: list, mine: list):
    score = 0
    for i in range(len(mine)):
        if mine[i] in valid:
            if score == 0:
                score += 1
            else:
                score *= 2
    return score

class Card:
    def __init__(self, card_str: str): # example: "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
        card = line.strip().split(":")
        game = card[1].split("|")

        self.id = card[0].split(" ")[1]
        self.valid = parse_digits_str(game[0])
        self.mine = parse_digits_str(game[1])
        self.amount = 1

    def score(self):
        return compare_digits(self.valid, self.mine)
    
    def winning_numbers(self):
        score = 0
        for i in range(len(self.mine)):
            if self.mine[i] in self.valid:
                score += 1
        return score

# Part 1
card_sum_values = 0

for line in lines:
    card = Card(line.strip())
    card_sum_values += card.score()

print("Part 1:", card_sum_values)

# Part 2

card_list = []
for line in lines:
    card = Card(line.strip())
    card_list.append(card)

for i in range(len(card_list)):
    for j in range(card_list[i].winning_numbers()):
        card_list[i+j+1].amount += card_list[i].amount
    

total_card_amount = 0;
for card in card_list:
    total_card_amount += card.amount

print("Part 2:", total_card_amount)