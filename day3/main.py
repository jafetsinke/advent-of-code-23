text_file = open('input.txt','r')
lines = text_file.readlines()
text_file.close()

class Schematic:
    def __init__(self, lines):
        self.schematic = []
        for line in lines:
            line = line.strip()
            chars = list(line)
            self.schematic.append(chars)

        self.height = len(self.schematic)
        self.width = len(chars)

    def get_coords(self, x, y):
        return self.schematic[y][x]
    
    def check_symbol_adjacent(self, x_coord, y_coord):
        # check if the symbol at x,y is adjacent to a symbol, returns boolean
        found_symbol = False
        neighbours = self.find_neighbours(x_coord, y_coord)
        for char in neighbours:
            if is_symbol(char):
                found_symbol = True
                break
        return found_symbol
    
    def find_neighbours(self, x_coord, y_coord) -> str:
        neighbours = ""

        for x in range(x_coord - 1, x_coord + 2):
            for y in range(y_coord - 1, y_coord + 2):
                if x == x_coord and y == y_coord:
                    continue
                if x < 0 or y < 0:
                    continue
                if x >= self.width or y >= self.height:
                    continue

                char = self.get_coords(x, y)
                neighbours += char
        
        return neighbours
    
    def find_adjacent_part_nums(self, x_coord, y_coord) -> list:
        
        part_nums = []

        for y in range(y_coord - 1, y_coord + 2):
            for x in range(x_coord - 1, x_coord + 2):
                if x == x_coord and y == y_coord:
                    continue
                if x < 0 or y < 0:
                    continue
                if x >= self.width or y >= self.height:
                    continue

                char = self.get_coords(x, y)
                if char.isdigit():
                    part = self.find_full_part(x, y)
                    part_nums.append(part)


        return list(set(part_nums))
        
    def find_full_part(self, x_coord, y_coord) -> str:
        part_num = self.get_coords(x_coord, y_coord)
        line = self.schematic[y_coord]

        x = x_coord + 1
        while x < self.width:
            char = line[x]
            if char.isdigit():
                part_num += char
            else:
                break
            x += 1

        x = x_coord - 1
        while x >= 0:
            char = line[x]
            if char.isdigit():
                part_num = char + part_num
            else:
                break
            x -= 1

        return part_num


    def draw(self):
        visual = ""
        for line in self.schematic:
            visual += "".join(line) + "\n"

        return visual

    def __repr__(self):
        return f"Width: {self.width}, Height: {self.height}\n{self.draw()}"
    

def is_symbol(symbol: str):
    if symbol == ".":
        return False
    elif symbol.isdigit():
        return False
    else:
        return True

schema = Schematic(lines)
print(schema)

# Part 1
parts = []
for y, line in enumerate(schema.schematic):
    part_amount = 0
    current_part = ""
    part_valid = False
    for x, char in enumerate(line):
        if char.isdigit():
            current_part += char
            if schema.check_symbol_adjacent(x, y):
                
                part_valid = True
        
        if (char == ".") or (is_symbol(char)) or (x == schema.width - 1):
            if part_valid:
                parts.append(current_part)

            current_part = ""
            part_valid = False
            continue
        

print("part 1", sum([int(part) for part in parts]))

# Part 2 
sum_gear_ratio = 0
for y, line in enumerate(schema.schematic):
    for x, char in enumerate(line):
        if is_symbol(char):
            adjacent_parts = schema.find_adjacent_part_nums(x, y)
            if (len(adjacent_parts) == 2):
                gear_ratio = int(adjacent_parts[0]) * int(adjacent_parts[1])
                sum_gear_ratio += gear_ratio

# print(schema.find_adjacent_part_nums(9, 1))
print("part 2", sum_gear_ratio)
