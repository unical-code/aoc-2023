# Description: Advent of Code Day 5 - Part 2

# TO DO: Optimize code to run faster

def getDest(n, lines):
    for i in range(len(lines)):
        if int(lines[i][1]) <= n and int(lines[i][1]) + int(lines[i][2]) >= n:
            return int(lines[i][0]) + n - int(lines[i][1])
    return n

def main():
    min = []
    seeds = []

    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []


    # Open input file
    f = open("day5/input.txt", "r")

    line = f.readline()

    seedSubstring = line.split(": ")[1].split(" ")
    seedSubstring[len(seedSubstring) - 1] = seedSubstring[len(seedSubstring) - 1].replace("\n", "")

    for i in range(0, len(seedSubstring), 2):
        for j in range(int(seedSubstring[i + 1])):
            seeds.append(int(seedSubstring[i]) + j)
            print(int(seedSubstring[i]) + j)


    line = f.readline()
    line = f.readline()
    line = f.readline()
    while line != "\n":
        seed_to_soil.append(line.split(" "))
        seed_to_soil[len(seed_to_soil) - 1][2] = seed_to_soil[len(seed_to_soil) - 1][2].replace("\n", "")
        line = f.readline()

    line = f.readline()
    line = f.readline()
    while line != "\n":
        soil_to_fertilizer.append(line.split(" "))
        soil_to_fertilizer[len(soil_to_fertilizer) - 1][2] = soil_to_fertilizer[len(soil_to_fertilizer) - 1][2].replace("\n", "")
        line = f.readline()

    line = f.readline()
    line = f.readline()
    while line != "\n":
        fertilizer_to_water.append(line.split(" "))
        fertilizer_to_water[len(fertilizer_to_water) - 1][2] = fertilizer_to_water[len(fertilizer_to_water) - 1][2].replace("\n", "")
        line = f.readline()

    line = f.readline()
    line = f.readline()
    while line != "\n":
        water_to_light.append(line.split(" "))
        water_to_light[len(water_to_light) - 1][2] = water_to_light[len(water_to_light) - 1][2].replace("\n", "")
        line = f.readline()

    line = f.readline()
    line = f.readline()
    while line != "\n":
        light_to_temperature.append(line.split(" "))
        light_to_temperature[len(light_to_temperature) - 1][2] = light_to_temperature[len(light_to_temperature) - 1][2].replace("\n", "")
        line = f.readline()

    line = f.readline()
    line = f.readline()
    while line != "\n":
        temperature_to_humidity.append(line.split(" "))
        temperature_to_humidity[len(temperature_to_humidity) - 1][2] = temperature_to_humidity[len(temperature_to_humidity) - 1][2].replace("\n", "")
        line = f.readline()

    line = f.readline()
    line = f.readline()
    while line != "":
        humidity_to_location.append(line.split(" "))
        humidity_to_location[len(humidity_to_location) - 1][2] = humidity_to_location[len(humidity_to_location) - 1][2].replace("\n", "")
        line = f.readline()

    for s in seeds:
        soil = getDest(int(s), seed_to_soil)
        fertilizer = getDest(int(soil), soil_to_fertilizer)
        water = getDest(fertilizer, fertilizer_to_water)
        light = getDest(water, water_to_light)
        temperature = getDest(light, light_to_temperature)
        humidity = getDest(temperature, temperature_to_humidity)
        location = getDest(humidity, humidity_to_location)
        min.append(location)

    solution = min[0]
    for i in range(1, len(min)):
        if min[i] < solution:
            solution = min[i]

    print(solution)


main()