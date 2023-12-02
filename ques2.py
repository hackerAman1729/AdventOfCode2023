def is_game_possible(game_info, max_red, max_green, max_blue):
  sets = game_info.split('; ')
  for set_info in sets:
      red = green = blue = 0
      if 'red' in set_info:
          red = int(set_info.split(' red')[0].split()[-1])
      if 'green' in set_info:
          green = int(set_info.split(' green')[0].split()[-1])
      if 'blue' in set_info:
          blue = int(set_info.split(' blue')[0].split()[-1])

      if red > max_red or green > max_green or blue > max_blue:
          return False

  return True

def sum_of_possible_games(file_path, max_red, max_green, max_blue):
  total_sum = 0
  possible_games = []

  with open(file_path, 'r') as file:
      for line in file:
          game_id, game_info = line.split(': ')
          game_id = int(game_id.split(' ')[1])

          if is_game_possible(game_info, max_red, max_green, max_blue):
              total_sum += game_id
              possible_games.append(game_id)

  print(f"Possible Games: {possible_games}")
  return total_sum

file_path = 'day2.txt'
max_red = 12
max_green = 13
max_blue = 14

result = sum_of_possible_games(file_path, max_red, max_green, max_blue)
print(f"Sum of IDs of Possible Games: {result}")


# part 2

def calculate_min_cubes_and_power(game_info):
  min_red = min_green = min_blue = 0

  sets = game_info.split('; ')
  for set_info in sets:
      red = green = blue = 0
      if 'red' in set_info:
          red = int(set_info.split(' red')[0].split()[-1])
      if 'green' in set_info:
          green = int(set_info.split(' green')[0].split()[-1])
      if 'blue' in set_info:
          blue = int(set_info.split(' blue')[0].split()[-1])

      min_red = max(min_red, red)
      min_green = max(min_green, green)
      min_blue = max(min_blue, blue)

  power = min_red * min_green * min_blue

  return power

def sum_of_powers(file_path):
  total_power_sum = 0

  with open(file_path, 'r') as file:
      for line in file:
          game_info = line.split(': ')[1]

          power = calculate_min_cubes_and_power(game_info)
          total_power_sum += power

  return total_power_sum


result = sum_of_powers(file_path)
print(f"Sum of Power: {result}")
