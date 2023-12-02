from Day2Input import puzzle_input

def find_possible_games(games_record):
    
    divided_lines = games_record.split('\n')

    games = []
    for line in divided_lines:
        sets = line.split(': ')[1]
        divided_sets = sets.split('; ')
        found_red_cubes, found_green_cubes, found_blue_cubes = 0, 0, 0
        for set in divided_sets:
            divided_set = set.split(', ')
            for item in divided_set:
                if 'red' in item:
                    red_cubes = int(item.split(' ')[0])
                    if red_cubes > found_red_cubes:
                        found_red_cubes = red_cubes
                elif 'green' in item:
                    green_cubes = int(item.split(' ')[0])
                    if green_cubes > found_green_cubes:
                        found_green_cubes = green_cubes
                elif 'blue' in item:
                    blue_cubes = int(item.split(' ')[0])
                    if blue_cubes > found_blue_cubes:
                        found_blue_cubes = blue_cubes
        power_of_set = found_red_cubes * found_green_cubes * found_blue_cubes
        games.append(power_of_set)
    
    return sum(games)


test_string = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

print(find_possible_games(test_string))
print(find_possible_games(puzzle_input))
