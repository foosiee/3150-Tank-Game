import turtle
from Utilites import get_filename
from TankManager import TankManager
from Sprites import Sprites

class Tank(turtle.Turtle):
    def __init__(self, team="User", start_pos=(0,0), direction=None, manager=None, id=0):
        super().__init__()
        self.manager = manager
        self.color = 'red' if team == 'Computer' else 'green'
        self.team = team
        self.grid = manager.get_grid()
        self.gridX = start_pos[0]
        self.gridY = start_pos[1]

        self.sprites = Sprites(team, direction)
        self.sprite = self.sprites.get_curr_sprite()

        self.coords = [0,0] # could abstract more lines 10-13
        self.health = 100 #100 = max health 0 = dead
        self.id = id # not sure what conditonal to use yet maybe a uuid
        self.active = True

        self.draw(self.sprite)
        self.up()
        self.move(self.gridX, self.gridY)

        self.disabled = False

    def is_inbounds(self, x, y):
        return x >= 0 and x < len(self.grid[0]) and y >=0 and y < len(self.grid)

    def set_grid_coords(self, x, y):
        self.set_gridX(x)
        self.set_gridY(y)

    def set_gridX(self, x):
        self.gridX = x

    def set_gridY(self, y):
        self.gridY = y

    def move(self, x, y):
        if self.is_inbounds(x, y):
            coords = self.grid.get_coords(x,y)
            self.goto(coords)
            self.set_grid_coords(x, y)
            self.manager.update_tank_on_grid(self)

    def move_up(self):
        if not self.disabled:
            newY = self.gridY - 1
            self.move(self.gridX, newY)

    def move_down(self):
        if not self.disabled:
            newY = self.gridY + 1
            self.move(self.gridX, newY)

    def move_left(self):
        if not self.disabled:
            newX = self.gridX - 1
            self.move(newX, self.gridY)

    def move_right(self):
        if not self.disabled:
            newX = self.gridX + 1
            self.move(newX, self.gridY)

    def rotate_right(self):
        if not self.disabled:
            self.sprite = self.sprites.get_next_sprite()
            self.draw(self.sprite)

    def rotate_left(self):
        if not self.disabled:
            self.sprite = self.sprites.get_prev_sprite()
            self.draw(self.sprite)

    def draw(self, asset):
        self.shape(asset)

    def aim_bot(self):
        self.disabled = True
        closest_tank = self.manager.get_closest_tank(self)
        diff_x = abs(closest_tank.xcor() - self.xcor())
        diff_y = abs(closest_tank.ycor() - self.ycor())

        if diff_x < diff_y:
            self.goto(closest_tank.xcor(),self.ycor())
        else:
            self.goto(self.xcor(), closest_tank.ycor())

        if closest_tank.ycor() < self.ycor():
            self.sprite = self.sprites.get_down_sprite()
        elif closest_tank.ycor() > self.ycor():
            self.sprite = self.sprites.get_up_sprite()          
        elif closest_tank.xcor() < self.xcor():
            self.sprite = self.sprites.get_left_sprite()
        else:
            self.sprite = self.sprites.get_right_sprite()
        
        self.disabled = False
        self.draw(self.sprite)