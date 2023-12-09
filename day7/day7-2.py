# Description: Advent of Code Day 7 - part 1

val = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def getType(string):
    three = False
    two = 0
    jolly = string.count("J")
    if jolly == 5:
        return 1
    for i in range(5):
        if string[i] == "J":
            continue
        if string.count(string[i]) + jolly == 5:
            return 1
        if string.count(string[i]) + jolly == 4:
            return 2
        if string.count(string[i]) == 3:
            three = True
        elif string.count(string[i]) + jolly == 3:
            two += 1
        if string.count(string[i]) == 2:
            two += 1
    if three and two == 2:
        return 3
    elif three:
        return 4
    elif two == 4:
        return 5
    elif two == 2:
        return 6
    else:
        return 7

def comparator(a, b):
    typeA = getType(a[0])
    typeB = getType(b[0])
    if typeA < typeB:
        return True
    elif typeA > typeB:
        return False
    else:
        for i in range(5):
            if a[0][i] == b[0][i]:
                continue
            else:
                if val.index(a[0][i]) < val.index(b[0][i]):
                    return True
                else:
                    return False
                
def sortHands(hands):
    for i in range(len(hands)):
        for j in range(i+1, len(hands)):
            if comparator(hands[i], hands[j]):
                temp = hands[i]
                hands[i] = hands[j]
                hands[j] = temp
    return hands

def main():
    f = open("day7/input.txt", "r")
    res = 0
    hands = []
    line = f.readline().strip()

    while line != "":
        hands.append([line.split(" ")[0], int(line.split(" ")[1])])
        getType(line.split(" ")[0])
        line = f.readline().strip()

    hands = sortHands(hands)
    for i in range(len(hands)):
        res += hands[i][1] * (i + 1)

    #for i in range(len(hands)):
    #    print(hands[i][0])

    print(res)

main()