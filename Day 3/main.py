path = "/Users/parthaupadhya/Coding/Python/Advent of Code/Day 3/input.txt"

def sumOfPriorities(inputList) -> int:
    sum = 0
    for letter in inputList:
        if letter.isupper():
            sum += ord(letter) - 38
        elif letter.islower():
            sum += ord(letter) - 96    
    
    return sum

inputFile = open(path)
lines = [line.rstrip() for line in inputFile]

repeats = list()

for line in lines:
    # Splits the line into halves
    backpacksize = int(len(line))
    first_half = line[0 : int((backpacksize/2))]
    second_half = line[int(backpacksize/2): int(backpacksize)]
    
    # Compares each letter in the first half with each in the second, adding to the "repeats" list if the letter is repeated.
    temp = list()
    for letter1 in first_half:
        for letter2 in second_half:
            if letter1 == letter2:
                if letter1 not in temp:
                    repeats.append(letter1)
                    temp.append(letter1)
        
print("Sum of priorities = " + str(sumOfPriorities(repeats)))

group_badges = list()
i = 0
while i < len(lines) - 2:
    temp = list()
    for letter1 in lines[i]:
        for letter2 in lines[i + 1]:
            if letter1 == letter2:
                for letter3 in lines[i + 2]:
                    if letter1 == letter3 and letter2 == letter3 and letter3 not in temp:
                        group_badges.append(letter1)
                        temp.append(letter1)
                        break

    i += 3

print("Sum of badge priorities = " + str(sumOfPriorities(group_badges)))

inputFile.close()