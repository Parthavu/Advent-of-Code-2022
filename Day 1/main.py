inputFile = open(r"/Users/parthaupadhya/Coding/Python/Advent of Code/Day 1/input.txt", "r")

lines = [line.rstrip() for line in inputFile]

sum = 0
cals = list()

for line in lines:
    if len(line) != 0:
        sum += int(line)
    
    else:
        cals.append(sum)
        sum = 0

print("The maximum number of calories carried by an elf is: " + str(max(cals)))

cals.sort()

sum2 = 0
for x in range(3):
    indexMax = cals.index(max(cals))
    sum2 += cals[indexMax]
    cals.pop(indexMax)

print("Combined calories of the top 3 elves are: " + str(sum2))
inputFile.close()