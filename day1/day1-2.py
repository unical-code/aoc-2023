# Description: Advent of Code Day 1 - Part 2

# Numbers in words
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0
string = ""

# Open input file
f = open("input.txt", "r")

# Read each line of input file
string = f.readline()
while string != "":
    first = -1
    last = -1   

    # Save position of first digit
    posfirst = len(string)

    # Find first and last digit
    for i in range(len(string)):

        # Check if digit
        if string[i].isdigit():
            if first == -1 and posfirst > i:
                first = int(string[i])
                posfirst = i
            last = int(string[i])
        
        # Check if number in words (one, two, three, etc.)
        for j in range(len(numbers)):

            # Check if number in words starts at position i
            if string[i:].startswith(numbers[j]):
                if first == -1 and posfirst > i:
                    first = j + 1
                    posfirst = i
                last = j + 1

    # Merge first and last digit and add to total
    sum += int(str(first) + str(last))
    string = f.readline()

# Close input file
f.close()

# Print total (solution)
print(sum)
    