import turtle
from Tank import Tank

class Game:
    def start(self):
        self.wn = turtle.Screen()
        self.wn.bgcolor("white") #can remove probs
        self.wn.setup(width=1000, height=800)
        self.wn.bgpic('Assets/Game/background.gif')


        self.wn.title('Tank Battle')
        
        teams = ["User", "Computer"]

        for team in teams:
            self.wn.register_shape(f'Assets/{team}/tank.gif')
            self.wn.register_shape(f'Assets/{team}/tankright.gif')
            self.wn.register_shape(f'Assets/{team}/tankleft.gif')
            self.wn.register_shape(f'Assets/{team}/tankdown.gif')

        user_tank = Tank(start_pos=(-349,0), direction="R")
        computer_tank = Tank(team="Computer", start_pos=(349, 0), direction="L")

        self.wn.listen()
        self.wn.onkeypress(user_tank.move_up, "Up")
        self.wn.onkeypress(user_tank.move_down, 'Down')
        self.wn.onkeypress(user_tank.move_right, 'Right')
        self.wn.onkeypress(user_tank.move_left, 'Left')
        self.wn.onkeypress(user_tank.rotate_right, 'e')
        self.wn.onkeypress(user_tank.rotate_left, 'q')

        while True:
            self.wn.update()

g = Game()
g.start()