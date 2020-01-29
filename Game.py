import turtle
from Tank import Tank

class Game:
    def start(self):
        self.wn = turtle.Screen()
        self.wn.bgcolor("white")
        self.wn.setup(width=800, height=600)

        self.wn.title('Tank Battle')
        
        teams = ["User", "Computer"]

        for team in teams:
            self.wn.register_shape(f'Assets/{team}/tank.gif')
            self.wn.register_shape(f'Assets/{team}/tankright.gif')
            self.wn.register_shape(f'Assets/{team}/tankleft.gif')
            self.wn.register_shape(f'Assets/{team}/tankdown.gif')

        tank = Tank(teams[0])

        self.wn.listen()
        self.wn.onkeypress(tank.move_up, "w")
        self.wn.onkeypress(tank.move_down, 's')
        self.wn.onkeypress(tank.move_right, 'd')
        self.wn.onkeypress(tank.move_left, 'a')
        self.wn.onkeypress(tank.rotate_right, 'e')
        self.wn.onkeypress(tank.rotate_left, 'q')

        while True:
            self.wn.update()



g = Game()
g.start()