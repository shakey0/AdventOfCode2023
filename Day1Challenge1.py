from Day1Input import puzzle_input

def decode_calibration_values(lines_to_decode):
    
    divided_lines = lines_to_decode.split('\n')

    calibration_values = []
    
    for line in divided_lines:
        first_digit = next(char for char in line if char.isdigit())
        last_digit = next(char for char in reversed(line) if char.isdigit())
        full_number = int(first_digit + last_digit)
        calibration_values.append(full_number)
    return sum(calibration_values)

test_string = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

print(decode_calibration_values(test_string))
print(decode_calibration_values(puzzle_input))
