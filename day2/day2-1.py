# Description: Advent of Code Day 2 - Part 1

sum = 0
string = ""
maxRed = 12
maxGreen = 13
maxBlue = 14

# Open input file
f = open("day2/input.txt", "r")

# Read each line of input file
string = f.readline()
while string != "":
    testPassed = True
    # Get game ID
    gameID = string.split(":")[0].split("Game ")[1]

    # Get game rounds splitted
    gameRounds = string.split(": ")[1].split("; ")

    # Check each round of the game
    for i in range(0, len(gameRounds)):

        # Get each set of the round
        setComponents = gameRounds[i].split(", ")

        # Check if the set is valid
        for j in range(0, len(setComponents)):
            token = setComponents[j].split(" ")
            if token[1] == "red":
                if int(token[0]) > maxRed:
                    testPassed = False
            elif token[1] == "green":
                if int(token[0]) > maxGreen:
                    testPassed = False
            elif token[1] == "blue":
                if int(token[0]) > maxBlue:
                    testPassed = False

    # If the game is valid, add the game ID to the sum
    if testPassed:
        sum += int(gameID)

    # Read next line
    string = f.readline()

# Close input file
f.close()

# Print result
print(sum)