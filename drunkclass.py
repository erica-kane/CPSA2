import matplotlib.pyplot as plt 

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
        doorx = minx + (self.width/2)
        self.door = (doorx, doory)


class House(Building):
    def __init__(self, number, coords):
        super().__init__(coords)
        self.number = number

    def draw(self, fig, ax):
        house_outline = plt.Rectangle(self.bl, self.width, self.height, fill=False)
        ax.add_patch(house_outline)
        plt.scatter(self.door[0], self.door[1], marker='s', s=1)


class Pub(Building):
    def draw(self, fig, ax):
        outline = plt.Rectangle(self.bl, self.width, self.height, fill=False, color='r')
        ax.add_patch(outline)
        plt.scatter(self.door[0], self.door[1], marker='s', s=1, c='r')


