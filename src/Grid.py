from GridNode import GridNode

class Grid:
    def __init__(self):
        self.grid = []
        self.__set_up_grid()

    def __set_up_grid(self):
        x = -300
        y = 400
        for _ in range(7):
            y-=100
            if x != -300:
                x = -300
            for _ in range(7):
                self.grid.append(GridNode((x,y)))
                x+=100