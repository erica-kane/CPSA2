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

    # def draw(self):
    #     info = self.build
    #     fig, ax = plt.subplots()
    #     house_outline = plt.Rectangle((info[0][0], info[0][1]), info[2], info[3], fill=False)
    #     ax.add_patch(house_outline)
    #     plt.axis('square')
    #     ax.autoscale_view()


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

