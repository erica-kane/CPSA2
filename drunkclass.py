import matplotlib
import matplotlib.pyplot as plt 
import drunkclass
import matplotlib.patches as patches
import random

class House():
    def __init__(self, number, coords): 
        self.number = number
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
        doorx = minx + (self.width/2)
        self.door = (doorx, doory)

    def draw(self, fig, ax):
        house_outline = plt.Rectangle(self.bl, self.width, self.height, fill=False)
        ax.add_patch(house_outline)
        plt.scatter(self.door[0], self.door[1], marker='s', s=1, c='k')


class Pub():
    def __init__(self, coords):
        self.coords = coords
    
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

        width = maxx - minx
        height = maxy - miny

        doory = miny
        doorx = minx + (width/2)
        
        binfo = [(minx, miny), (maxx, maxy), width, height, (doorx, doory)]
        return binfo

