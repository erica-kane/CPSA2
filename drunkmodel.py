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

for x, row in enumerate(plan):
    for y, value in enumerate(row):
        if value >= 10.0 and value <= 250.0:
            houses.append((x, y, value))





