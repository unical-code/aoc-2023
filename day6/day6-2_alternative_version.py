# Description: Advent of Code Day 6 - Part 1

from math import sqrt


def ways(t, d):
    # this is the result of the inequality: (t-x)*x>d -> x^2 - tx + d < 0
    # the values needed are the result of the associated equation
    delta = t * t - 4 * d
    min_v = (t - sqrt(delta)) // 2
    max_v = (t + sqrt(delta)) // 2
    return int(max_v - min_v)


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
        res *= ways(int(times[i]), int(distance[i]))

    # close the file
    f.close()

    # print the result
    print(res)


main()