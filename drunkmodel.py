import csv
import matplotlib
import matplotlib.pyplot as plt 
import drunkclass
import matplotlib.patches as patches
import random

plan = []
f = open('drunk.plan.txt', newline = '')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
plan = list(reader)
f.close()

y_len = len(plan)
x_len = len(plan[0])

plt.imshow(plan)
plt.show()

houses_info = []
houses_info_dict = {}
pub_info = []
houses = []


# Getting coordinates of each house point from the 'plan'
for y, row in enumerate(plan):
    for x, value in enumerate(row):
        if value >= 10.0 and value <= 250.0:
            houses_info.append([int(x), int(y), int(value)])


# Setting 'house numbers' as the keys of the dictionary, and empty lists as values
for row in houses_info:
    houses_info_dict[row[2]] = []
    
# Appending tuples of x and y values of the houses to the value lists in the dictionary
for row in houses_info:
    houses_info_dict[row[2]].append((row[0], row[1]))

## Below is first attempt of the above code, also works but is less efficient
# for key, value in houses_dict.items():
#     for row in houses:
#         if row[2] == key:
#             houses_dict[key].append((row[0], row[1]))

# Check the dictionary by comparing length of each list of coordinates
# to how many house number 30's there were in houses and plan
for key, value in houses_info_dict.items():
    print(len(value))

practice = []
for row in houses_info:
    if row[2] == 30:
        practice.append(row[2])
len(practice)       

practicetwo = []
for row in plan:
    for value in row:
        if value == 240:
            practicetwo.append(value)
len(practicetwo)

# All show 121 coordinates per house, which suggests an 11x11 area


# Getting coordinates of pub point from the 'plan' and appending to a list of tuples 
for y, row in enumerate(plan):
    for x, value in enumerate(row):
        if value == 1.0:
            pub_info.append((int(x), int(y)))
len(pub_info)
# length 441, suggesting 21x21 grid 


# Make the houses 
for number, coords in houses_info_dict.items():
    houses.append(drunkclass.House(number, coords))

# Make the pub 
pub = drunkclass.Pub(pub_info)

pubbuild = pub.build()

# Testing points 
for house in houses:
    plt.scatter(house.bl[0], house.bl[1], s=1)
    plt.scatter(house.tr[0], house.tr[1], s=1)

plt.scatter(pubbuild[0][0], pubbuild[0][1], s=1, c="r")
plt.scatter(pubbuild[1][0], pubbuild[1][1], s=1, c='r')


# line 110 was taken from below website 
# https://stackoverflow.com/questions/37435369/matplotlib-how-to-draw-a-rectangle-on-image
fig, ax = plt.subplots()

for house in houses:
    house_outline = plt.Rectangle(house.bl, house.width, house.height, fill=False)
    ax.add_patch(house_outline)
    plt.scatter(house.door[0], house.door[1], marker='s', s=1, c='k')

pub_outline = plt.Rectangle((pubbuild[0][0], pubbuild[0][1]), pubbuild[2], pubbuild[3], fill=False, color='r')
ax.add_patch(pub_outline)
plt.scatter(pubbuild[4][0], pubbuild[4][1], marker='s', s=1, c='r')

plt.axis('square')
ax.autoscale_view()


