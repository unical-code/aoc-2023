# Description: Advent of Code Day 2 - Part 2

sum = 0
string = ""

# Open input file
f = open("day2/input.txt", "r")

# Read each line of input file
string = f.readline()
while string != "":

    # Get min values
    minRed = 0
    minGreen = 0
    minBlue = 0

    # Get game rounds splitted
    gameRounds = string.split(": ")[1].split("; ")

    # Check each round of the game
    for i in range(0, len(gameRounds)):

        # Get each set of the round
        setComponents = gameRounds[i].split(", ")

        # Get min values for each component
        for j in range(0, len(setComponents)):
            token = setComponents[j].split(" ")
            if token[1].startswith("red"):
                if int(token[0]) > minRed:
                    minRed = int(token[0])
            elif token[1].startswith("green"):
                if int(token[0]) > minGreen:
                    minGreen = int(token[0])
            elif token[1].startswith("blue"):
                if int(token[0]) > minBlue:
                    minBlue = int(token[0])

    # Add the product of the min values to the sum
    sum += (minRed * minGreen * minBlue)

    # Read next line
    string = f.readline()

# Close input file
f.close()

# Print result
print(sum)