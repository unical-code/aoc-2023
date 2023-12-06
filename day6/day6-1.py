# Description: Advent of Code Day 6 - Part 1

def main():
    res = 1
    f = open("day6/input.txt", "r")
    line = f.readline().strip()

    # get the times
    times = line.split("Time:")[1].split(" ")
    while "" in times:
        times.remove("")
    
    # get the distances
    line = f.readline().strip()
    distance = line.split("Distance:")[1].split(" ")
    while "" in distance:
        distance.remove("")

    # get the number of possible winning combinations
    for i in range(len(times)):
        pos = 0
        for j in range(int(times[i])):
            if int(distance[i]) <= int(int(times[i]) - j) * j:
                pos += 1
        # multiply the number of possible winning combinations for each race
        res *= pos

    # close the file
    f.close()

    # print the result
    print(res)

main()