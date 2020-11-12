import matplotlib.pyplot as plt 
import random

class Building():
    def __init__(self, coords): 
        self.coords = coords
        self.build()
    
    def build(self):
        xvalues = []
        yvalues = []

        for coord in self.coords:
            xvalues.append(coord[0])
        minx = min(xvalues)
        maxx = max(xvalues)

        for coord in self.coords:
            yvalues.append(coord[1])
        miny = min(yvalues)
        maxy = max(yvalues)

        self.bl = (minx, miny)
        self.tr = (maxx, maxy)

        self.width = maxx - minx
        self.height = maxy - miny

        doory = miny
        doorx = minx + int(self.width/2)
        self.door = (doorx, doory)

        centrex = doorx
        centrey = miny + int(self.height/2)
        self.centre = (centrex, centrey)


class House(Building):
    def __init__(self, number, coords):
        super().__init__(coords)
        self.number = number
        yvalues = []
        for coord in self.coords:
            yvalues.append(coord[1])
        doory = max(yvalues)
        doorx = self.door[0]
        self.backdoor = (doorx, doory)

    def draw(self):
        house_outline = plt.Rectangle(self.bl, self.width, self.height, fill=False)
        plt.gca().add_patch(house_outline)
        plt.gca().text(self.tr[0], self.tr[1], str(self.number))
        plt.scatter(self.door[0], self.door[1], marker='s', s=1, c='k')
        plt.scatter(self.backdoor[0], self.backdoor[1], marker='s', s=1, c='k')
        


class Pub(Building):
    def draw(self):
        outline = plt.Rectangle(self.bl, self.width, self.height, fill=False, color='r')
        plt.gca().add_patch(outline)
        plt.gca().text(self.tr[0], self.tr[1], 'Pub', color = 'r')
        plt.scatter(self.door[0], self.door[1], marker='s', s=1, c='r')



class Drunk():
    def __init__(self, x, y, drunks, plan, home):
        self.x = x
        self.y = y
        self.drunks = drunks
        self.plan = plan 
        self.home = home
        self.y_max = len(plan) - 1
        self.x_max = len(plan[0]) - 1

# Find distance between drunk and door 
    def find_distance_home(self):
        distance_door = (((self.x - self.home.door[0])**2) + ((self.y - self.home.door[1])**2))**0.5
        distance_backdoor = (((self.x - self.home.backdoor[0])**2) + ((self.y - self.home.backdoor[1])**2))**0.5
        distance = min(distance_backdoor, distance_door)
        return distance

# Random walk
    def walk_random(self):
        if random.random() < 0.5:
            nexty = (self.y + 1)
        else:
            nexty = (self.y - 1)

        if random.random() < 0.5:
            nextx = (self.x + 1)
        else:
            nextx = (self.x - 1)
        return (nextx, nexty)

    def walk_home(self):
        diff_x = self.home.door[0] - self.x
        # door to the right
        if diff_x > 0:
            nextx = (self.x + 1)
        # door to the left
        elif diff_x < 0:
            nextx = (self.x - 1)
        # at the door
        else:
            nextx = self.x

        diff_y = self.home.door[1] - self.y
        # door to the bottom
        if diff_y > 0:
            nexty = (self.y + 1)
        # door to the top
        elif diff_y < 0:
            nexty = (self.y - 1)
        # at the door 
        else:
            nexty = self.y
        return (nextx, nexty)

    def walk(self):
        if self.find_distance_home() >= 110:
            nextx, nexty = self.walk_random()
        else:
            if random.random() < 0.3:
                nextx, nexty = self.walk_random()
            else:
                nextx, nexty = self.walk_home()

# Boundary check for perimeter 
        if nextx < 0:
            nextx = 0
        elif nextx > self.x_max:
            nextx = self.x_max
        
        if nexty < 0:
            nexty = 0
        elif nexty > self.y_max:
            nexty = self.y_max

# Boundary checking for buildings 
        building_value = self.plan[nexty][nextx]
        if building_value == 0:
            self.x = nextx
            self.y = nexty
        elif (nextx, nexty) == (self.home.door[0], self.home.door[1]):
            self.x = nextx
            self.y = nexty

# Getting home 
        if self.x == self.home.door[0] and self.y == self.home.door[1]:
            self.drunks.remove(self)

    def draw(self):
        plt.scatter(self.x, self.y)