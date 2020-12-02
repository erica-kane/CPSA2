import matplotlib.pyplot as plt 
import random

def calculate_distance(p1, p2):
    """Calculates the distance between two points

    Args:
        p1 (tuple): (x ,y) of first point
        p2 (tuple): (x, y) of second point
    
    >>> calculate_distance((1,1), (1,1))
    0.0
    >>> calculate_distance((52, 3), (26, 77))
    78.43468620451031
    """

    x1, y1 = p1
    x2, y2 = p2
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return distance


class Drunk():
    def __init__(self, x, y, drunks, plan, home, townmap):
        """Generates a drunk.

        Args:
            x (number): x coordinate 
            y (number): y coordinate
            drunks (list): list of all drunks 
            plan (2D list): the given environment 
            home (House): the House to which the drunk is attributed 
            townmap (2D list): map of movements made 
        """
        self.x = x
        self.y = y
        self.drunks = drunks
        self.plan = plan 
        self.home = home
        self.townmap = townmap
        self.target = self.home.door
        self.y_max = len(plan) - 1
        self.x_max = len(plan[0]) - 1

    def find_distance_target(self):
        """Finds the distance between a drunk and their target. 

        Returns:
            Number: Result of distance calculation.
        """
        return calculate_distance((self.x, self.y), self.target)


    def walk_random(self):
        """Moves drunk randomly (left/right, up/down).

        Returns:
            tuple: next x and y coordinates.
        """
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
        """Moves drunk in the direction of their home's door.

        Returns:
            tuple: next x and y coordinates.
        """
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


    def walk(self):
        """Moves the drunk 90% randomly if the distance to their door is more than or equal to 50.
        Moves the drunk 30% randomly if the distance to their door is less than 50. 
        Makes a boundary check for the perimeter and houses so drunks don't walk through buildings.
        Re-targets if the drunk gets stuck on a perimeter.
        Removes drunk from list once it reaches its door. 
        """
        if self.find_distance_target() >= 50:
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
        # Pre emptive check, if the drunk will hit a town wall, don't move there 
        if nextx < 0:
            nextx = 0
        elif nextx > self.x_max:
            nextx = self.x_max
        
        if nexty < 0:
            nexty = 0
        elif nexty > self.y_max:
            nexty = self.y_max

        # Boundary checking for buildings 
        # Pre emptive check, if the drunk will walk somewhere on the plan that is denoted by a 0
        # UNLESS the value is the door, in that case the drunk can have access, or
        # if you're going to walk somewhere that isn't denoted by a 0, it is a building and you will be blocked
        # If that is the case, the drunk retargets, moving to a random location within a 40x40 radius of the blockage 
        # After reaching the new target, it sets the target back as door and tries again 
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
            print(f'Drunk number {self.home.number} got home')
            self.drunks.remove(self)

    def add_to_map(self):
        """Adds 1 when drunk passes a point on the map.
        """
        self.townmap[self.y][self.x] += 1

    def draw(self):
        """Draws drunks.
        """
        plt.scatter(self.x, self.y, c='b')

