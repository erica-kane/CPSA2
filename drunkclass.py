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

    def draw(self, fig, ax):
        house_outline = plt.Rectangle(self.bl, self.width, self.height, fill=False)
        ax.add_patch(house_outline)
        ax.text(self.tr[0], self.tr[1], str(self.number))
        plt.scatter(self.door[0], self.door[1], marker='s', s=1, c='k')
        


class Pub(Building):
    def draw(self, fig, ax):
        outline = plt.Rectangle(self.bl, self.width, self.height, fill=False, color='r')
        ax.add_patch(outline)
        ax.text(self.tr[0], self.tr[1], 'Pub', color = 'r')
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


    def walk(self):
        if random.random() < 0.5:
            nexty = (self.y + 1)
        else:
            nexty = (self.y - 1)

        if random.random() < 0.5:
            nextx = (self.x + 1)
        else:
            nextx = (self.x - 1)


        if nextx < 0:
            nextx = 0
        elif nextx > self.x_max:
            nextx = self.x_max
        
        if nexty < 0:
            nexty = 0
        elif nexty > self.y_max:
            nexty = self.y_max


        building_value = self.plan[nexty][nextx]
        if building_value == 0:
            self.x = nextx
            self.y = nexty


        if self.x == self.home.door[0] and self.y == self.home.door[1]:
            self.drunks.remove(self)

    def draw(self):
        plt.scatter(self.x, self.y)