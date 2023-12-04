def calculate_points(scratchcards):
  total_points = 0
  for card in scratchcards:
      parts = card.strip().split('|')
      winning_numbers = set(map(int, parts[0].split()[2:]))  # Extract winning numbers
      your_numbers = list(map(int, parts[1].split()))  # Extract my numbers

      matches = 0
      for num in your_numbers:
          if num in winning_numbers:
              matches += 1

      if matches > 0:
          points = 2 ** (matches - 1)
          total_points += points

  return total_points

def calculate_total_scratchcards(scratchcards):
  cards_data = []
  for card in scratchcards:
      parts = card.strip().split('|')
      winning_numbers = set(map(int, parts[0].split()[2:]))
      your_numbers = list(map(int, parts[1].split()))
      cards_data.append((winning_numbers, your_numbers))

  card_copies = [1] * len(cards_data)

  for i in range(len(cards_data)):
      for _ in range(card_copies[i]):
          matches = len(cards_data[i][0].intersection(cards_data[i][1]))
          for j in range(i + 1, min(i + 1 + matches, len(cards_data))):
              card_copies[j] += 1

  total_scratchcards = sum(card_copies)
  return total_scratchcards

file_path = 'day4/day4.txt'
with open(file_path, 'r') as file:
  scratchcards = file.readlines()

print("Total points:", calculate_points(scratchcards))
print("Total scratchcards:", calculate_total_scratchcards(scratchcards))
