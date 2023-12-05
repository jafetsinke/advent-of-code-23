# this works with the sample input but performance is horrible, hence the rewriting in main2.py

text_file = open('test.txt','r')
lines = text_file.readlines()
lines = [line.strip() for line in lines]
text_file.close()

# parse the first line and convert to array of seed numbers
seeds_to_plant = lines[0].strip()
seeds_to_plant = seeds_to_plant.split(':')[1].strip().split(' ')
lines = lines[1:]

seed_maps = {}

current_map = None
for i in range(len(lines)):
    if lines[i] == '': continue
    if ':' in lines[i]: # it defines a new map
        map_name = lines[i].split('map:')[0].strip()
        current_map = map_name
        seed_maps[map_name] = {}
    else: # its a line of the map
        seed_numbers = lines[i].split(' ')
        destination_range_start = int(seed_numbers[0])
        source_range_start = int(seed_numbers[1])
        range_length = int(seed_numbers[2])
        for i in range(range_length):
            map_from = source_range_start + i
            map_to = destination_range_start + i
            seed_maps[current_map][map_from] = map_to

def lookup_seed(seed, maps):
    
    num = seed;
    for map_name in maps:
        print(f'looking up seed: {str(seed)} in map: {map_name}')
        if maps[map_name].get(num) != None:
            num = maps[map_name][num]
    return num

lowest_location = None
for seed in seeds_to_plant:
    location = lookup_seed(int(seed), seed_maps)
    if lowest_location == None:
        lowest_location = location
    else:
        lowest_location = min(lowest_location, location)

print('lowest location: ' + str(lowest_location))


test_seeds = {
    79: 82,
    14: 43,
    55: 86,
    13: 35
}

def test(test_seeds):
    for seed, soil in test_seeds.items():
        if lookup_seed(seed, seed_maps) != soil:
            print('failed for seed: ' + str(seed))
        else:
            print('passed for seed: ' + str(seed))

#test(test_seeds)