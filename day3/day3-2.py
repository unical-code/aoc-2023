# Description: Advent of Code Day 3 - Part 2

# check if the character at index is a number
def isNumber(string, index):
    if index > len(string) - 1 or index < 0:
        return False
    if string[index].isdigit():
        return True
    else:
        return False
    

# Create a number made by the digits around the index
def CunstructNumber(string, index):
    if not isNumber(string, index):
        return 1
    number = string[index]
    rIndex = index
    index += 1
    while isNumber(string, index):
        number += string[index]
        index += 1
    index = rIndex
    index -= 1
    while isNumber(string, index):
        number = string[index] + number
        index -= 1
    return number

# check if the gear has 2 numbers around it
def lookAround(middle, upper, lower, index):
    n = 0
    tot = 1
    if isNumber(middle, index-1):
        n += 1
        tot *= int(CunstructNumber(middle, index-1))
    if isNumber(middle, index+1):
        n += 1
        tot *= int(CunstructNumber(middle, index+1))
    if isNumber(upper, index-1):
        n += 1
        tot *= int(CunstructNumber(upper, index-1))
        if not isNumber(upper, index) and isNumber(upper, index+1):
            n += 1
            tot *= int(CunstructNumber(upper, index+1))
    elif isNumber(upper, index+1):
        n += 1
        tot *= int(CunstructNumber(upper, index+1))
    elif isNumber(upper, index):
        n += 1
        tot *= int(CunstructNumber(upper, index))
    
    if isNumber(lower, index-1):
        n += 1
        tot *= int(CunstructNumber(lower, index-1))
        if not isNumber(lower, index) and isNumber(lower, index+1):
            n += 1
            tot *= int(CunstructNumber(lower, index+1))
    elif isNumber(lower, index+1):
        n += 1
        tot *= int(CunstructNumber(lower, index+1))
    elif isNumber(lower, index):
        n += 1
        tot *= int(CunstructNumber(lower, index))
    if n == 2:
        return tot
    else:
        return 0
    
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
    for i in range(len(middle)):
        if middle[i] == '*':
            sum += lookAround(middle, upper, lower, i)
    upper = middle
    middle = lower
    lower = f.readline()

# Close input file
f.close()

# Print result
print(sum)
                








