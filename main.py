# Imports the module to print a random choice from strings, can be removed if 'strings = random.choice(strings)' is removed
import random

# Base list, can add items before hand or keep it empty to only output the document
strings = []

# Appends every line of the document and strips it of unnecessary formats
file = open('text.txt', 'r')
for line in file:
  stng = line.strip()
  strings.append(stng)

# Remove this line of code to just print the list and not one random
strings = random.choice(strings)

# Prints the final result of list
print(strings)
