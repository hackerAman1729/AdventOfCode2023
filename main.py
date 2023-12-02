import re

def calculate_calibration_sum(file_path):
    total_sum = 0
    number_words = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    words_to_digits = dict(zip(number_words, digits))

    with open(file_path, 'r') as file:
        for line in file:
            pattern = r"(?=(" + "|".join(number_words + digits) + "))"
            matches = re.findall(pattern, line)
            found = [words_to_digits.get(match, match) for match in matches]

            if found:
                first_digit = found[0]
                last_digit = found[-1]
                line_value = int(first_digit + last_digit)
                total_sum += line_value

    return total_sum

file_path = 'ques1.txt'

calibration_sum = calculate_calibration_sum(file_path)
print(calibration_sum)


