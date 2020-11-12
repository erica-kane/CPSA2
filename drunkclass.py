import matplotlib.pyplot as plt 
import random

class Drunk():
    def __init__(self, x, y, drunks, plan, home):
        self.x = x
        self.y = y
        self.drunks = drunks
        self.plan = plan 
        self.home = home
        self.target = self.home.door
        self.y_max = len(plan) - 1
        self.x_max = len(plan[0]) - 1

# Find distance between drunk and door 
    def find_distance_target(self):
        distance = (((self.x - self.target[0])**2) + ((self.y - self.target[1])**2))**0.5
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

# Walking directly home 
    def walk_home(self):
        diff_x = self.target[0] - self.x
        # door to the right
        if diff_x > 0:
            nextx = (self.x + 1)
        # door to the left
        elif diff_x < 0:
            nextx = (self.x - 1)
        # at the door
        else:
            nextx = self.x

        diff_y = self.target[1] - self.y
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

# Walking route 
    def walk(self):
        if self.find_distance_target() >= 110:
            if random.random() < 0.1:
                nextx, nexty = self.walk_home()
            else:
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
        elif (nextx, nexty) == self.home.door:
            self.x = nextx
            self.y = nexty
        else:
            targetx = self.home.door[0] + random.randint(-20, 20)
            targety = self.home.door[1] + random.randint(-20, 20)
            self.target = (targetx, targety)
        
        if (self.x, self.y) == self.target:
            self.target = self.home.door

# Getting home 
        if self.x == self.home.door[0] and self.y == self.home.door[1]:
            self.drunks.remove(self)

    def draw(self):
        plt.scatter(self.x, self.y, c='b')