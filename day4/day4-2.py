# Description: Advent of Code Day 4 - Part 2

def main():
    # Open input file
    f = open("day4/input.txt", "r")
    tot = 0

    # Read each line of input file
    lines = f.readlines()
    addedScratchcards = []

    # Get winning count for each line
    for i in range(0, len(lines)):
        addedScratchcards.append(winningCount(lines[i]))
    
    # Get the number of generated scratchcards from each scratchcard
    for i in range(0, len(lines)):
        tot += getPoint(addedScratchcards, i) + 1

    # Close input file
    f.close()

    # Print result
    print(tot)

# Get the number of generated scratchcards from each scratchcard (recursive)
def getPoint(addedScratchcards, id):
    sum = 0
    num = addedScratchcards[id]
    sum += num
    for i in range(1, num  + 1):
        sum += getPoint(addedScratchcards, id + i)
    return sum

# Get the number of winning numbers in a line (part 1)
def winningCount(line):
    winningNumbers = line.split(": ")[1].split(" | ")[0].split(" ")
    ticketNumbers = line.split(": ")[1].split(" | ")[1].split(" ")

    while "" in winningNumbers:
        winningNumbers.remove("")

    while "" in ticketNumbers:
        ticketNumbers.remove("")

    ticketNumbers[len(ticketNumbers) - 1] = ticketNumbers[len(ticketNumbers) - 1].replace("\n", "")

    win = 0

    for i in range(0, len(ticketNumbers)):
        if ticketNumbers[i] in winningNumbers:
            win += 1
    return win

main()