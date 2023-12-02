from Day2Input import puzzle_input

def find_possible_games(games_record, red=None, green=None, blue=None):
    
    divided_lines = games_record.split('\n')

    possible_games = []
    for line in divided_lines:
        game_number = int(line.split(': ')[0].split(' ')[1])
        sets = line.split(': ')[1]
        divided_sets = sets.split('; ')
        set_valid = True
        for set in divided_sets:
            divided_set = set.split(', ')
            for item in divided_set:
                if 'red' in item:
                    red_cubes = int(item.split(' ')[0])
                    if red:
                        if red_cubes > red:
                            set_valid = False
                elif 'green' in item:
                    green_cubes = int(item.split(' ')[0])
                    if green:
                        if green_cubes > green:
                            set_valid = False
                elif 'blue' in item:
                    blue_cubes = int(item.split(' ')[0])
                    if blue:
                        if blue_cubes > blue:
                            set_valid = False
        if set_valid:
            possible_games.append(game_number)
    
    return sum(possible_games)






test_string = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

print(find_possible_games(test_string, 12, 13, 14))
print(find_possible_games(puzzle_input, 12, 13, 14))