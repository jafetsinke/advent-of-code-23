text_file = open('input.txt','r')
lines = text_file.readlines()
lines = [line.strip() for line in lines]
text_file.close()

class NumMap:
    def __init__(self, map_str: str):
        seed_numbers = map_str.split(' ')
        self.destination_range_start = int(seed_numbers[0])
        self.source_range_start = int(seed_numbers[1])
        self.range_length = int(seed_numbers[2])

    def __repr__(self) -> str:
        return f'<NumMap: {self.destination_range_start}, {self.source_range_start}, {self.range_length}>'
    
    def in_map(self, num: int):
        return self.source_range_start <= num < self.source_range_start + self.range_length
    
    def convert_num(self, num: int):
        if not self.in_map(num):
            return num
        
        num_pos = num - self.source_range_start
        return self.destination_range_start + num_pos

class SeedMap:
    def __init__(self, map_name, map_chunk):
        self.map_from = map_name.split('-to-')[0]
        self.map_to = map_name.split('-to-')[1]
        self.mapping = [NumMap(num_map) for num_map in map_chunk]

    def __repr__(self) -> str:
        return f'<SeedMap: {self.map_from} to {self.map_to}>'
    
    def find_num(self, num: int):
        current_num = num
        for num_map in self.mapping:
            if not num_map.in_map(current_num): continue
            
            current_num = num_map.convert_num(current_num)
            break

        return current_num

def lookup_seed(seed, maps: [SeedMap]):
    num = seed
    for seed_map in maps:
        num = seed_map.find_num(num)
    return num

# parse the first line and convert to array of seed numbers
seeds_to_plant = lines[0].strip()
seeds_to_plant = seeds_to_plant.split(':')[1].strip().split(' ')
lines = lines[1:]

# create parsable chunks for every seed map
seed_map_chunks = {}
for i in range(len(lines)):
    if lines[i] == '': continue
    if ':' in lines[i]: # it defines a new map
        map_name = lines[i].split('map:')[0].strip()
        current_map = map_name
        seed_map_chunks[map_name] = []
    else: # its a line of the map
        seed_map_chunks[current_map].append(lines[i])

# create seed map instances for every chunk
seed_maps = [SeedMap(map_name, chunk) for map_name, chunk in seed_map_chunks.items()]

def find_lowest_seed_location(seeds: [int], seed_maps: [SeedMap]):
    lowest_location = None
    for seed in seeds:
        location = lookup_seed(int(seed), seed_maps)
        if lowest_location == None:
            lowest_location = location
        else:
            lowest_location = min(lowest_location, location)

    return lowest_location

def find_lowest_seed_location_range(start: int, end: int, seed_maps: [SeedMap]):
    lowest_location = None
    for seed in range(start, end):
        location = lookup_seed(int(seed), seed_maps)
        if lowest_location == None:
            lowest_location = location
        else:
            lowest_location = min(lowest_location, location)

    return lowest_location

# part 1
print('lowest location: ' + str(find_lowest_seed_location(seeds_to_plant, seed_maps)))

# part 2 



# small test to check if code is working properly
test_seeds = {
    79: 82,
    14: 43,
    55: 86,
    13: 35
}

def test(test_seeds):
    for seed, soil in test_seeds.items():
        result = lookup_seed(seed, seed_maps)
        if result != soil:
            print(f'failed for seed: {str(seed)} got: {result} expected: {soil}')
        else:
            print('passed for seed: ' + str(seed))

#test(test_seeds)