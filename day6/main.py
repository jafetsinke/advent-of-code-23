class Game:
    def __init__(self, time: int, distance: int):
        self.time = time
        self.record_distance = distance

    def __repr__(self):
        return f'<Game(time={self.time}, distance={self.record_distance})>'
    
    def cal_possible_wins(self):
        wins = []
        for i in range(0, self.time):
            distance = self.cal_game_outcome(i)
            if self.record_distance < distance:
                wins.append(i)
        return wins
    
    def cal_game_outcome(self, buttom_time: int) -> int:
        time_left = self.time - buttom_time
        speed = buttom_time
        distance = speed * time_left
        return distance


text_file = open('input.txt','r')
lines = text_file.readlines()
lines = [line.strip() for line in lines]
text_file.close()


for i in range(len(lines)):
    if lines[i] == '': continue
    num_string = lines[i].split(':')[1].strip().split(' ')

    num_array = []
    for j in range(len(num_string)):
        if num_string[j] == '': continue
        num_array.append(int(num_string[j]))

    lines[i] = num_array

times = lines[0]
distances = lines[1]
games = []

if len(times) != len(distances):
    raise Exception('times and distances must be the same length')

# part 1
for i in range(len(times)):
    games.append(Game(times[i], distances[i]))

multiplied_possible_wins = None
for game in games:
    wins = len(game.cal_possible_wins())
    if multiplied_possible_wins == None:
        multiplied_possible_wins = wins
    else:
        multiplied_possible_wins *= wins

print('part 1:', multiplied_possible_wins)


# part 2
time = ''.join((str(t) for t in times))
distance = ''.join((str(d) for d in distances))
game = Game(int(time), int(distance))
print("part 2:", len(game.cal_possible_wins()))