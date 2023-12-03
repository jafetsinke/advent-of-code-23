class Game: 
    # example input: "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    def __init__(self, line: str):
        game = line.split(":")
        self.game_id = int(game[0].replace("Game ", ""))

        rounds_str = game[1].split(";")
        self.rounds = [CubeSet(round) for round in rounds_str]

    def min_cubeset(self):
        cube_set = CubeSet("0 red, 0 green, 0 blue")

        for round in self.rounds:
            if round.red > cube_set.red:
                cube_set.red = round.red
            if round.green > cube_set.green:
                cube_set.green = round.green
            if round.blue > cube_set.blue:
                cube_set.blue = round.blue

        return cube_set


    def __repr__(self):
        return f"Game ID: {self.game_id}, Rounds: {self.rounds}"

class CubeSet:
    # example input: "3 blue, 4 red"
    def __init__(self, cubes: str):
        self.red = 0
        self.green = 0
        self.blue = 0

        cubes = cubes.split(",")
        cubes = [cube.strip() for cube in cubes]

        for cube in cubes:
            cube = cube.split(" ")
            if cube[1] == "red":
                self.red = int(cube[0])
            elif cube[1] == "green":
                self.green = int(cube[0])
            elif cube[1] == "blue":
                self.blue = int(cube[0])

    def power(self):
        return self.red * self.green * self.blue

    def __repr__(self):
        return f"Red: {self.red}, Green: {self.green}, Blue: {self.blue}"


text_file = open('input.txt','r')
lines = text_file.readlines()
text_file.close()

bag_contains = {
    "red": 12,
    "green": 13,
    "blue": 14
}

# part 1
sum_possible_game_ids = 0
for line in lines:
    game = Game(line)
    game_possible = True
    for round in game.rounds:
        if round.red > bag_contains["red"] or round.green > bag_contains["green"] or round.blue > bag_contains["blue"]:
            game_possible = False
            continue
    
    if game_possible:
        sum_possible_game_ids += game.game_id

print("Part 1:", sum_possible_game_ids)

# part 2
sum_powers = 0
for line in lines:
    game = Game(line)
    power = game.min_cubeset().power()
    sum_powers += power

print("Part 2:", sum_powers)