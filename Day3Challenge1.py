from Day3Input import puzzle_input

def find_adjecent_symbols(listed_chars, column_count, row_count):
    search_area = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, -1], [-1, 1], [1, 1], [1, -1]]
    symbols = ['+', '*', '=', '-', '&', '#', '/', '%', '$', '@']
    for space in search_area:
        try:
            if listed_chars[row_count + space[0]][column_count + space[1]] in symbols:
                return True
        except IndexError:
            pass
    return False

def get_all_part_numbers(engine_schematic):

    divided_lines = engine_schematic.split('\n')

    listed_chars = []
    for line in divided_lines:
        listed_chars.append(list(line))

    found_digits = []
    row_count = 0
    while row_count < len(listed_chars):
        column_count = 0
        finding_digit = False
        found_digit = ""
        found_symbol = []
        while column_count < len(listed_chars[row_count]):
            if listed_chars[row_count][column_count].isdigit():
                finding_digit = True
                found_digit += listed_chars[row_count][column_count]
                symbol = find_adjecent_symbols(listed_chars, column_count, row_count)
                found_symbol.append(symbol)
            else:
                if finding_digit:
                    if any(found_symbol):
                        found_digits.append(int(found_digit))
                    finding_digit = False
                    found_digit = ""
                    found_symbol = []
            column_count += 1
        if finding_digit:
            if any(found_symbol):
                found_digits.append(int(found_digit))
        row_count += 1
    return sum(found_digits)
    

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

print(get_all_part_numbers(test_string))
print(get_all_part_numbers(puzzle_input))


# def get_all_symbols(input):
#     symbols = []
#     for line in input.split('\n'):
#         for char in line:
#             if char != '.' and not char.isdigit() and char not in symbols:
#                 symbols.append(char)
#     print(symbols)

# get_all_symbols(puzzle_input)
