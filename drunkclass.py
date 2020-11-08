

class House():
    def __init__(self, number, coords): 
        self.number = number
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
        binfo = [(minx, miny), (maxx, maxy), width, height]
        return binfo
        

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
        binfo = [(minx, miny), (maxx, maxy), width, height]
        return binfo
