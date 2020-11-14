import matplotlib.pyplot as plt 
import random

# Creating building superclass
# This will be in common for the pub and houses
# Initialises with its coordinates, and is attributed a door and necessary values to plot 
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


# House subclass, initialised with its number and coordinates, as well as the superclass initialisation 
# Draw method given which makes plotting in the final figure easier
    # Plots the rectangle outline and the door 
    # Gives an option for including the house numbers as text on the figure 
class House(Building):
    def __init__(self, number, coords):
        super().__init__(coords)
        self.number = number

    def draw(self, number=True):
        house_outline = plt.Rectangle(self.bl, self.width, self.height, fill=False)
        plt.gca().add_patch(house_outline)
        if number:
            plt.gca().text(self.tr[0], self.tr[1], str(self.number))
        plt.scatter(self.door[0], self.door[1], marker='s', s=1, c='k')        

# Pub subclass (no more initialisation steps than proivded by the super class)
# Draw method, different to House draw method as it is red, and the text is a label, not number 
class Pub(Building):
    def draw(self, text=True):
        outline = plt.Rectangle(self.bl, self.width, self.height, fill=False, color='r')
        plt.gca().add_patch(outline)
        if text:
            plt.gca().text(self.tr[0], self.tr[1], 'Pub', color = 'r')
        plt.scatter(self.door[0], self.door[1], marker='s', s=1, c='r')

