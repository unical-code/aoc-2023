# Description: Advent of Code Day 5 - Part 1

# Function to get the conversion from idA to idB
def getDest(n, lines):
    for i in range(len(lines)):
        if int(lines[i][1]) <= n and int(lines[i][1]) + int(lines[i][2]) >= n:
            return int(lines[i][0]) + n - int(lines[i][1])
    return n

def main():
    min = []

    # List of conversion lines
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

    # Get the seeds
    seeds = line.split(": ")[1].split(" ")
    seeds[len(seeds) - 1] = seeds[len(seeds) - 1].replace("\n", "")

    # Get the conversions from seeds to soil
    line = f.readline()
    line = f.readline()
    line = f.readline()
    while line != "\n":
        seed_to_soil.append(line.split(" "))
        seed_to_soil[len(seed_to_soil) - 1][2] = seed_to_soil[len(seed_to_soil) - 1][2].replace("\n", "")
        line = f.readline()

    # Get the conversions from soil to fertilizer
    line = f.readline()
    line = f.readline()
    while line != "\n":
        soil_to_fertilizer.append(line.split(" "))
        soil_to_fertilizer[len(soil_to_fertilizer) - 1][2] = soil_to_fertilizer[len(soil_to_fertilizer) - 1][2].replace("\n", "")
        line = f.readline()

    # Get the conversions from fertilizer to water
    line = f.readline()
    line = f.readline()
    while line != "\n":
        fertilizer_to_water.append(line.split(" "))
        fertilizer_to_water[len(fertilizer_to_water) - 1][2] = fertilizer_to_water[len(fertilizer_to_water) - 1][2].replace("\n", "")
        line = f.readline()

    # Get the conversions from water to light
    line = f.readline()
    line = f.readline()
    while line != "\n":
        water_to_light.append(line.split(" "))
        water_to_light[len(water_to_light) - 1][2] = water_to_light[len(water_to_light) - 1][2].replace("\n", "")
        line = f.readline()

    # Get the conversions from light to temperature
    line = f.readline()
    line = f.readline()
    while line != "\n":
        light_to_temperature.append(line.split(" "))
        light_to_temperature[len(light_to_temperature) - 1][2] = light_to_temperature[len(light_to_temperature) - 1][2].replace("\n", "")
        line = f.readline()

    # Get the conversions from temperature to humidity
    line = f.readline()
    line = f.readline()
    while line != "\n":
        temperature_to_humidity.append(line.split(" "))
        temperature_to_humidity[len(temperature_to_humidity) - 1][2] = temperature_to_humidity[len(temperature_to_humidity) - 1][2].replace("\n", "")
        line = f.readline()

    # Get the conversions from humidity to location
    line = f.readline()
    line = f.readline()
    while line != "":
        humidity_to_location.append(line.split(" "))
        humidity_to_location[len(humidity_to_location) - 1][2] = humidity_to_location[len(humidity_to_location) - 1][2].replace("\n", "")
        line = f.readline()

    # Get the location of each seed
    for s in seeds:
        soil = getDest(int(s), seed_to_soil)
        fertilizer = getDest(int(soil), soil_to_fertilizer)
        water = getDest(fertilizer, fertilizer_to_water)
        light = getDest(water, water_to_light)
        temperature = getDest(light, light_to_temperature)
        humidity = getDest(temperature, temperature_to_humidity)
        location = getDest(humidity, humidity_to_location)
        min.append(location)

    # find the minimum location
    solution = min[0]
    for i in range(1, len(min)):
        if min[i] < solution:
            solution = min[i]


    # Close input file
    f.close()

    # Print the solution
    print(solution)


main()