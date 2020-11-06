import csv
import matplotlib
import matplotlib.pyplot


plan = []
f = open('drunk.plan.txt', newline = '')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
plan = list(reader)
f.close()

len(plan)
len(plan[0])

matplotlib.pyplot.imshow(plan)
matplotlib.pyplot.show()


housenumbers = [float(i) for i in list(range(10, 260, 10))]
houses = []
houses_dict = {}

for x, row in enumerate(plan):
    for y, value in enumerate(row):
        if value >= 10.0 and value <= 250.0:
            houses.append([int(x), int(y), int(value)])


# Setting 'house numbers' as the keys of the dictionary, and empty lists as values
for row in houses:
    houses_dict[row[2]] = []
    
# Appending tuples of x and y values of the houses to the value lists in the dictionary
for row in houses:
    houses_dict[row[2]].append((row[0], row[1]))

## Below is first attempt of the above code, also works but is less efficient
# for key, value in houses_dict.items():
#     for row in houses:
#         if row[2] == key:
#             houses_dict[key].append((row[0], row[1]))

# Check the dictionary by comparing length of each list of coordinates
# to how many house number 30's there were in houses and plan
for key, value in houses_dict.items():
    print(len(value))

practice = []
for row in houses:
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

