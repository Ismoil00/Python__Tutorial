import math;

# converting kilograms to pounds:
def kg_to_lbs(weight):
  return math.ceil(int(weight) / 0.45)

# finding max number from the list of numbers:
def find_max(list_of_numbers):
  max_number = list_of_numbers[0]

  for number in list_of_numbers:
    if number > max_number:
      max_number = number

  return max_number