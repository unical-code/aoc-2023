# Description: Advent of Code Day 1 - Part 1

sum = 0
string = ""

# Open input file
f = open("day1/input.txt", "r")

# Read each line of input file
string = f.readline()
while string != "":
    first = -1
    last = -1    

    # Find first and last digit
    for i in range(len(string)):
        if string[i].isdigit():
            if first == -1:
                first = string[i]
            last = string[i]

    # Merge first and last digit and add to total
    sum += int(first + "" + last)
    string = f.readline()

# Close input file
f.close()

# Print total (solution)
print(sum)
    