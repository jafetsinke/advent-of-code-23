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

card_sum_values = 0
# Part 1
for line in lines:
    card = line.strip().split("|")
    card_valid = parse_digits_str(card[0].split(":")[1])
    card_mine = parse_digits_str(card[1])
    card_score = compare_digits(card_valid, card_mine)
    card_sum_values += card_score

print("Part 1:", card_sum_values)
