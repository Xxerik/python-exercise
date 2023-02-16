
inputFile = open("input.txt")
inputCalories = inputFile.read().split("\n")
currentHighest = 0
current = 0

for i in inputCalories:
    if(i == ""):
        if (current > currentHighest):
            currentHighest = current
        current = 0
    else:
        current += int( i )
print(currentHighest)
