import random

def Convert(string): 
    li = list(string.split(" ")) 
    return li 

strings = []

file = open('text.txt', 'r')
for line in file:
  stng = line.strip()
  strings.append(stng)

strings = random.choice(strings)
print(strings)