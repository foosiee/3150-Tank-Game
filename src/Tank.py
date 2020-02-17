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

        self.sprites = Sprites(team, direction)
        self.sprite = self.sprites.get_curr_sprite()

        self.coords = [0,0] # could abstract more lines 10-13
        self.health = 100 #100 = max health 0 = dead
        self.id = id # not sure what conditonal to use yet maybe a uuid
        self.active = True

        self.draw(self.sprite)
        self.up()
        self.goto(start_pos[0], start_pos[1])

        self.disabled = False

    def move_up(self):
        if not self.disabled:
            if self.ycor() <= 290:
                self.sety(self.ycor()+60)

    def move_down(self):
        if not self.disabled:
            if self.ycor() >= -290:
                self.sety(self.ycor()-60)

    def move_left(self):
        if not self.disabled:
            if self.xcor() > -350:
                self.setx((self.xcor()-60))

    def move_right(self):
        if not self.disabled:
            if self.xcor() <= 380:
                self.setx((self.xcor()+60))

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