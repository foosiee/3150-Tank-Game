from GridNode import GridNode

class Grid:
    def __init__(self):
        self.grid = []
        self.__set_up_grid()

    def __getitem__(self, key):
        return self.grid[key]

    def __len__(self):
        return len(self.grid)

    def get_coords(self, x, y):
        if x < len(self.grid) and y < len(self.grid):
            return self.grid[y][x].coords

    def __set_up_grid(self):
        x = -300
        y = 400
        for _ in range(7):
            arr = []
            y-=100
            for _ in range(7):
                arr.append(GridNode((x,y)))
                x+=100
            x = -300
            self.grid.append(arr)