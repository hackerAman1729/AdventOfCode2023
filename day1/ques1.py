import re


def calculate_calibration_sum_part1(file_path):
  total_sum = 0
  with open(file_path, 'r') as file:
      for line in file:
          digits = []
          for char in line:
              if char.isdigit():
                  digits.append(char)
          if digits:
              first_digit = digits[0]
              last_digit = digits[-1]
              number = int(first_digit + last_digit)
              total_sum += number

  return total_sum



def calculate_calibration_sum_part2(file_path):
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

file_path = 'day1/ques1.txt'
print(f"{calculate_calibration_sum_part1(file_path)}")
print(f"{calculate_calibration_sum_part2(file_path)}")




