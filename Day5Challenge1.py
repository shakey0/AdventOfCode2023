from Day5Input import puzzle_input

class CalculateRanges:

    def __init__(self, input):
        sections = input.split('\n\n')
        seeds = sections[0].split(': ')[1].split()
        self.seeds = [int(seed) for seed in seeds]
        self.seed_to_soil_map = sections[1].split(':\n')[1].split('\n')
        self.find_seed_to_soil_map = self.get_corresponding_destination(self.seed_to_soil_map)
        self.soil_to_fertilizer_map = sections[2].split(':\n')[1].split('\n')
        self.find_soil_to_fertilizer_map = self.get_corresponding_destination(self.soil_to_fertilizer_map)
        self.fertilizer_to_water_map = sections[3].split(':\n')[1].split('\n')
        self.find_fertilizer_to_water_map = self.get_corresponding_destination(self.fertilizer_to_water_map)
        self.water_to_light_map = sections[4].split(':\n')[1].split('\n')
        self.find_water_to_light_map = self.get_corresponding_destination(self.water_to_light_map)
        self.light_to_temperature_map = sections[5].split(':\n')[1].split('\n')
        self.find_light_to_temperature_map = self.get_corresponding_destination(self.light_to_temperature_map)
        self.temperature_to_humidity_map = sections[6].split(':\n')[1].split('\n')
        self.find_temperature_to_humidity_map = self.get_corresponding_destination(self.temperature_to_humidity_map)
        self.humidity_to_location_map = sections[7].split(':\n')[1].split('\n')
        self.find_humidity_to_location_map = self.get_corresponding_destination(self.humidity_to_location_map)
    
    def get_corresponding_destination(self, map):
        corresponding_destination = []
        for line in map:
            line = line.split(' ')
            corresponding_destination.append([[int(line[1]), int(line[1])+(int(line[2])-1)], [int(line[0]), int(line[0])+(int(line[2])-1)]])
        return corresponding_destination

def find_corresponding_destination(item, row):
    for row in row:
        if item >= row[0][0] and item <= row[0][1]:
            return row[1][0] + (item - row[0][0])
    return item

def get_lowest_location_number(input):
    calculate_ranges = CalculateRanges(input)
    locations = []
    for seed in calculate_ranges.seeds:
        range = calculate_ranges.find_seed_to_soil_map
        soil = find_corresponding_destination(seed, range)
        range = calculate_ranges.find_soil_to_fertilizer_map
        fertilizer = find_corresponding_destination(soil, range)
        range = calculate_ranges.find_fertilizer_to_water_map
        water = find_corresponding_destination(fertilizer, range)
        range = calculate_ranges.find_water_to_light_map
        light = find_corresponding_destination(water, range)
        range = calculate_ranges.find_light_to_temperature_map
        temperature = find_corresponding_destination(light, range)
        range = calculate_ranges.find_temperature_to_humidity_map
        humidity = find_corresponding_destination(temperature, range)
        range = calculate_ranges.find_humidity_to_location_map
        location = find_corresponding_destination(humidity, range)
        locations.append(location)
    return min(locations)


test_string = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''

print(get_lowest_location_number(test_string))
print(get_lowest_location_number(puzzle_input))
