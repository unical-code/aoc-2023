# Description: Advent of Code Day 4 - Part 1

sum = 0

# Open input file
f = open("day4/input.txt", "r")

# Read each line of input file
line = f.readline()

while line != "":
    # Split line into winning numbers and ticket numbers
    winningNumbers = line.split(": ")[1].split(" | ")[0].split(" ")
    ticketNumbers = line.split(": ")[1].split(" | ")[1].split(" ")

    # Remove empty strings from lists
    while "" in winningNumbers:
        winningNumbers.remove("")
    while "" in ticketNumbers:
        ticketNumbers.remove("")

    # Remove newline character from last element of ticketNumbers
    ticketNumbers[len(ticketNumbers) - 1] = ticketNumbers[len(ticketNumbers) - 1].replace("\n", "")

    win = 0

    # Check if ticket numbers are in winning numbers
    for i in range(0, len(ticketNumbers)):
        if ticketNumbers[i] in winningNumbers:
            win += 1
    
    # Add 2 ^ (win - 1) to sum
    if win > 0:
        sum += 2 ** (win - 1)

    # Read next line
    line = f.readline()

# Close input file
f.close()

# Print sum
print(sum)