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

        self.width = len(self.schematic)
        self.height = len(chars)

    def get_coords(self, x, y):
        return self.schematic[y][x]
    
    def check_symbol_adjacent(self, x_coord, y_coord):
        # check if the symbol at x,y is adjacent to a symbol, returns boolean
        found_symbol = False
        for x in range(x_coord - 1, x_coord + 2):
            for y in range(y_coord - 1, y_coord + 2):
                if x == x_coord and y == y_coord:
                    continue
                if x < 0 or y < 0:
                    continue
                if x >= self.width or y >= self.height:
                    continue

                char = self.get_coords(x, y)
                if is_symbol(char):
                    return True
            
        return found_symbol


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
                print("Part valid", current_part)
                parts.append(current_part)

            current_part = ""
            part_valid = False
            continue
        
                

print(parts)

print(sum([int(part) for part in parts]))