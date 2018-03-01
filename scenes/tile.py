class Tile:
    
    def __init__(self, path, x, y):
        self.path = path
        self.x = x
        self.y = y

    def getRealXY(self):
    	return ((self.x - 1)*50, (self.y - 1)*35+40)
