from Day3Input import puzzle_input

def find_full_number(listed_chars, column_count, row_count):
    full_number = listed_chars[row_count][column_count]
    listed_chars[row_count][column_count] = '.'
    count = 1
    while True:
        try:
            if listed_chars[row_count][column_count + count].isdigit():
                full_number += listed_chars[row_count][column_count + count]
                listed_chars[row_count][column_count + count] = '.'
                count += 1
            else:
                break
        except IndexError:
            break
    count = 1
    while True:
        try:
            if listed_chars[row_count][column_count - count].isdigit():
                full_number = listed_chars[row_count][column_count - count] + full_number
                listed_chars[row_count][column_count - count] = '.'
                count += 1
            else:
                break
        except IndexError:
            break
    return int(full_number)

def find_gear_ratio(listed_chars, column_count, row_count):
    search_area = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, -1], [-1, 1], [1, 1], [1, -1]]
    numbers = []
    for space in search_area:
        try:
            if listed_chars[row_count + space[0]][column_count + space[1]].isdigit():
                gear_ratio = find_full_number(listed_chars, column_count + space[1], row_count + space[0])
                listed_chars[row_count + space[0]][column_count + space[1]] = '.'
                numbers.append(gear_ratio)
        except IndexError:
            pass
    if len(numbers) == 2:
        return numbers[0] * numbers[1]

def get_all_gear_ratios(engine_schematic):

    divided_lines = engine_schematic.split('\n')

    listed_chars = []
    for line in divided_lines:
        listed_chars.append(list(line))

    found_gear_ratios = []
    row_count = 0
    while row_count < len(listed_chars):
        column_count = 0
        while column_count < len(listed_chars[row_count]):
            if listed_chars[row_count][column_count] == '*':
                gear_ratio = find_gear_ratio(listed_chars, column_count, row_count)
                if gear_ratio:
                    found_gear_ratios.append(gear_ratio)
            column_count += 1
        row_count += 1
    return sum(found_gear_ratios)


test_string = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

print(get_all_gear_ratios(test_string))
print(get_all_gear_ratios(puzzle_input))
