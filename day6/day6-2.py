# Description: Advent of Code Day 6 - Part 2

def main():
    res = 0
    f = open("day6/input.txt", "r")

    # get the times and distances
    line = f.readline().strip()
    time = line.split("Time:")[1].replace(" ", "")
    line = f.readline().strip()
    distance = line.split("Distance:")[1].replace(" ", "")

    # get the number of possible winning combinations
    for i in range(int(time) + 1):
        if int(distance) <= int(int(time) - i) * i:
            res += 1

    # close the file
    f.close()

    # print the result
    print(res)

main()