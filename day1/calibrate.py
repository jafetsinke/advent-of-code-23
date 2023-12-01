import re

text_file = open('input.txt','r')
lines = text_file.readlines()
text_file.close()

# Part 1
def calibrate(lines):
    sum = 0

    for i in range(len(lines)):
        clean_line = lines[i]
        # remove all non-numeric characters
        digits = [c for c in clean_line if c.isdigit()]
        if (len(digits) == 0):
            continue # skip lines with no digits
        first_digit = digits[0]
        last_digit = digits[-1]
        cal_value = first_digit + last_digit
        sum += int(cal_value)

    return sum

print("Part 1:", calibrate(lines))

# Part 2
def calibrate2(lines):
    sum = 0

    for i in range(len(lines)):
        clean_line = lines[i].strip()
        print(clean_line)
        digits = get_digits(clean_line)
        digits = list(digits.values())
        print(digits)
        if (len(digits) == 0):
            continue # skip lines with no digits
        first_digit = digits[0]
        last_digit = digits[-1]
        cal_value = first_digit + last_digit

        sum += int(cal_value)

    return sum

num_strings = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five":"5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def get_digits(string: str):
    numstrings_dict = {} # key: position in string, value: found digit

    # search for digits
    for char in string:
        if (not char.isdigit()):
            continue

        positions = re.finditer(char, string)
        positions = [m.start() for m in positions]

        for pos in positions:
            numstrings_dict[pos] = char

    # search for num_strings (e.g. "one", "two", etc.)
    for num_string, digit in num_strings.items():
        if (not num_string in string):
            continue

        positions = re.finditer(num_string, string)
        positions = [m.start() for m in positions]

        for pos in positions:
            numstrings_dict[pos] = digit

    print(numstrings_dict)

    sorted_keys = dict(sorted(numstrings_dict.items()))

    return sorted_keys

print("part 2:", calibrate2(lines))




