import matplotlib.pyplot as plt 
import random


class Building():
    """ Super class for House and Pub. Represents a building on a plot and stores properties about it.
    """
    def __init__(self, coords): 
        """Initilaising buildings with a set of coordinates. 

        Args:
            coords (list): Nested list of tuples containing x and y coordinates.
        """
        self.coords = coords
        self.build()
    
    def build(self):
        """ Calculates the bottom left, top right, width and height of the building, and assigns the door. 

        >>> b = Building([(1,1), (1, 2), (2, 1), (2, 2)])
        >>> b.bl
        (1, 1)
        >>> b.tr
        (2, 2)
        >>> b.width
        1
        >>> b.door
        (1, 1)
        """
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

        print(f"Properties: bottom left = {self.bl}, top right = {self.tr}, width = {self.width}, height = {self.height}, door = {self.door}")



class House(Building):
    def __init__(self, number, coords):
        """House subclass

        Args:
            number (number): Individual house number.
            coords (list): List of coordinates as tuples.
        """
        print(f"Building house {number}")
        super().__init__(coords)
        self.number = number


    def draw(self, number=True):
        """Draws the Houses.
        Adds on to the current plt plot.

        Args:
            number (bool, optional): Controls whether the house numbers should be drawn. Defaults to True.
        """
        house_outline = plt.Rectangle(self.bl, self.width, self.height, fill=False)
        plt.gca().add_patch(house_outline)
        if number:
            plt.gca().text(self.tr[0], self.tr[1], str(self.number))
        plt.scatter(self.door[0], self.door[1], marker='s', s=1, c='k')        


class Pub(Building):
    """Pub subclass

    Args:
        Building (superclass): initialised with superclass __init__
    """
    def draw(self, text=True):
        """Draws the pub.
        Adds on to the current plt plot.

        Args:
            text (bool, optional): Controls whether the label for the pub should be drawn. Defaults to True.
        """
        outline = plt.Rectangle(self.bl, self.width, self.height, fill=False, color='r')
        plt.gca().add_patch(outline)
        if text:
            plt.gca().text(self.tr[0], self.tr[1], 'Pub', color = 'r')
        plt.scatter(self.door[0], self.door[1], marker='s', s=1, c='r')
