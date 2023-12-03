# Description: Advent of Code Day 3 - Part 1

# check if the character at index is a number
def isSimbol(string, index):
    if index > len(string) - 1 or index < 0:
        return False
    if string[index].isdigit() or string[index] == "." or string[index] == '\n':
        return False
    return True


# check if the character has a simbol around it
def lookAround(middle, upper, lower, index):
    for i in range(-1, 2, 1):
        if isSimbol(upper, index + i) or isSimbol(lower, index + i):
            return True
    if isSimbol(middle, index+i) or isSimbol(middle, index-1):
        return True
    return False


sum = 0
upper = ""
middle = ""
lower = ""

# Open input file
f = open("day3/input.txt", "r")

# Read each line of input file
middle = f.readline()
lower = f.readline()

while middle != "":
    actualNumber = ""
    enclosed = False
    
    for i in range(len(middle)):
        # Check if the single digit is enclosed by simbols or if it has simbols around the number
        if(middle[i].isdigit()):
            actualNumber += middle[i]
            if enclosed or lookAround(middle, upper, lower, i):
                enclosed = True
        else:
            # If the number is enclosed by simbols, add it to the sum
            if enclosed and actualNumber != "":
                sum += int(actualNumber)
            enclosed = False
            actualNumber = ""
    
    # Update lines
    upper = middle
    middle = lower
    lower = f.readline()

# Close input file
f.close()

# Print result
print(sum)
                








