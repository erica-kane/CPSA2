import csv
import matplotlib.pyplot as plt 
import matplotlib.animation 
import drunkclass
import buildingclass
import numpy as np

# Create all objects that will need to be used in further code 
plan = []
houses_info = []
houses_info_dict = {}
pub_info = []
houses = []
drunks = []
townmap = []

# Read in town plan
f = open('drunk.plan.txt', newline = '')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
plan = list(reader)
f.close()

# Find and save dimensions of plan 
y_len = len(plan)
x_len = len(plan[0])

# Visualise the plan
plt.imshow(plan, origin='lower')
plt.title("Original town plan visualisation")
plt.show()
plt.close()

# Getting coordinates of each house point from the plan, save to a nested list 
# The list will contain a set of coordinates for each point on the house, followed by the house number
for y, row in enumerate(plan):
    for x, value in enumerate(row):
        if value >= 10.0 and value <= 250.0:
            houses_info.append([int(x), int(y), int(value)])


# Setting 'house numbers' as the keys of a dictionary, and empty lists as values
# Keys must be uniqie, so this solves problem of eliminating repeat house numbers and saving as individual values per house 
for row in houses_info:
    houses_info_dict[row[2]] = []
    
# Appending tuples of x and y values of the houses to the value lists in the dictionary
# This results in a dictionary of keys (house numbers) and associated values (all the coordinates which make up the hosue)
for row in houses_info:
    houses_info_dict[row[2]].append((row[0], row[1]))


# Getting coordinates of pub point from the 'plan' and appending to a list of tuples 
# A dictionary is not needed as there is only one pub, so no associated number is necessary
for y, row in enumerate(plan):
    for x, value in enumerate(row):
        if value == 1.0:
            pub_info.append((int(x), int(y)))
len(pub_info)
# length 441, suggesting 20x20 grid 


# Make the houses 
for number, coords in houses_info_dict.items():
    houses.append(buildingclass.House(number, coords))

# Make the pub 
pub = buildingclass.Pub(pub_info)

# Plotting bottom left, top right, numbers and labels to test the information is correct before moving on
for house in houses:
    plt.scatter(house.bl[0], house.bl[1], s=1)
    plt.scatter(house.tr[0], house.tr[1], s=1)
    plt.gca().text(house.tr[0], house.tr[1], str(house.number))

plt.scatter(pub.bl[0], pub.bl[1], s=1, c="r")
plt.scatter(pub.tr[0], pub.tr[1], s=1, c='r')
plt.gca().text(pub.tr[0], pub.tr[1], 'Pub', color = 'r')
plt.title("Bottom left and top right points of each building")
plt.axis('square')
plt.show()
plt.close()


# Create the drunks
for house in houses:
    drunks.append(drunkclass.Drunk(pub.door[0], pub.door[1], drunks, plan, house, townmap))

# # Animation code - not necessary for final product but essential in development stages 

# fig = matplotlib.pyplot.figure(figsize=(7, 7))

# def update(frame_number):
#     print("update")
#     fig.clear()  

#     for house in houses:
#         house.draw()
    
#     pub.draw()

#     for drunk in drunks:
#         drunk.walk()
#         drunk.draw()

# animation = matplotlib.animation.FuncAnimation(fig, update, interval = 1, repeat = False, frames = 10000)

# plt.show()


# Create empty array for heat map which has the same dimensions as plan
for num in range(y_len):
    maprow = []
    for num in range(x_len):
        maprow.append(0)
    townmap.append(maprow)

# moving drunks and adding to townmap for each movement, for as long as there are drunks not home 
# pritning total to check how many iterations it took 
total = 0
while drunks:
    total += 1
    for drunk in drunks:
        drunk.walk()
        drunk.add_to_map()
print(f"Total number of iterations for all drunks to get home: {total}")


# Plot the heat map using a numpy array version of townmap
# The logarithm of townmap is calculated to scale the values resulting in a more visually appealing map 
scaledmap = np.log(np.array(townmap))
plt.imshow(scaledmap, cmap='hot', interpolation='nearest', origin="lower")
for house in houses:
    house.draw(number=False)
pub.draw(text=False)
plt.title("Density plot of the paths taken by drunks from the pub to their door")
plt.show()

# Write out townmap to a csv file 
mapfile = open('townmapfile.csv', "w")
writer = csv.writer(mapfile)
writer.writerows(townmap)
mapfile.close()

