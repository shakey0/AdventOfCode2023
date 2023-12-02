from Day1Input import puzzle_input

def decode_calibration_values2(lines_to_decode):

    divided_lines = lines_to_decode.split('\n')

    calibration_values = []

    spelled_numbers_to_digits = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    count = 0
    while count < len(divided_lines):

        start_indexes = {}
        for spelled_number, digit in spelled_numbers_to_digits.items():
            if spelled_number in divided_lines[count]:
                start_indexes[divided_lines[count].find(spelled_number)] = spelled_number

        if start_indexes:
            min_start_index = min(start_indexes.keys())
            divided_lines[count] = divided_lines[count].replace(start_indexes[min_start_index], str(spelled_numbers_to_digits[start_indexes[min_start_index]]))
            
        start_indexes_reversed = {}
        for spelled_number, digit in spelled_numbers_to_digits.items():
            if spelled_number[::-1] in divided_lines[count][::-1]:
                start_indexes_reversed[divided_lines[count][::-1].find(spelled_number[::-1])] = spelled_number
                
        if start_indexes_reversed:
            min_start_index_reversed = min(start_indexes_reversed.keys())
            divided_lines[count] = divided_lines[count].replace(start_indexes_reversed[min_start_index_reversed], str(spelled_numbers_to_digits[start_indexes_reversed[min_start_index_reversed]]))

        first_digit = next(char for char in divided_lines[count] if char.isdigit())
        last_digit = next(char for char in reversed(divided_lines[count]) if char.isdigit())
        full_number = int(first_digit + last_digit)
        calibration_values.append(full_number)
        count += 1

    return sum(calibration_values)

test_string = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

print(decode_calibration_values2(test_string))
print(decode_calibration_values2(puzzle_input))
