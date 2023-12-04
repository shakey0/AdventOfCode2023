from Day4Input import puzzle_input

def get_numbers_as_list(input):
    numbers = []
    start, end = 0, 3
    while end <= len(input):
        numbers.append(int(input[start:end]))
        start += 3
        end += 3
    return numbers

def find_total_cards(scratchcards):

    divided_lines = scratchcards.split('\n')

    wins_for_lines = {line_no: 1 for line_no in range(1, len(divided_lines) + 1)}

    count = 1
    while count <= len(divided_lines):
        for num in range(wins_for_lines[count]):

            line = divided_lines[count-1]

            card_no = int(line.split(':')[0].split('d')[1].strip())

            winning_numbers = line.split(':')[1].split('|')[0]
            winning_numbers = get_numbers_as_list(winning_numbers)

            scratch_numbers = line.split(':')[1].split('|')[1]
            scratch_numbers = get_numbers_as_list(scratch_numbers)

            wins = 0
            for number in scratch_numbers:
                if number in winning_numbers:
                    wins += 1
            
            for num in range(card_no + 1, card_no + 1 + wins):
                wins_for_lines[num] += 1
            
        count += 1
    
    return sum(wins_for_lines.values())


test_string = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

print(find_total_cards(test_string))
print(find_total_cards(puzzle_input))
