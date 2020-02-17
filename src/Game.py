import turtle
from Tank import Tank
from TankManager import TankManager
from Utilites import get_filename, get_random_position

class Game:
    def start(self):
        self.wn = turtle.Screen()
        self.wn.bgcolor("white") #can remove probs
        self.wn.setup(width=1000, height=800)

        self.wn.bgpic(get_filename('../Assets/Game/background.gif'))
        self.wn.title('Tank Battle')
        
        teams = ["User", "Computer"]

        for team in teams:
            self.wn.register_shape(get_filename(f'../Assets/{team}/tank.gif'))
            self.wn.register_shape(get_filename(f'../Assets/{team}/tankright.gif'))
            self.wn.register_shape(get_filename(f'../Assets/{team}/tankleft.gif'))
            self.wn.register_shape(get_filename(f'../Assets/{team}/tankdown.gif'))

        manager = TankManager()

        bounds = (400, 400)

        user_tank = Tank(start_pos=(-349,0), direction="R", manager=manager)
        manager.add_tank(user_tank)

        computer_tank = Tank(team="Computer", start_pos=get_random_position(bounds), direction="L", manager=manager, id=1)
        manager.add_tank(computer_tank)

        computer_tank1 = Tank(team="Computer", start_pos=get_random_position(bounds), direction="L", manager=manager, id=2)
        manager.add_tank(computer_tank1)

        computer_tank2 = Tank(team="Computer", start_pos=get_random_position(bounds), direction="L", manager=manager, id=3)
        manager.add_tank(computer_tank2)

        computer_tank3 = Tank(team="Computer", start_pos=get_random_position(bounds), direction="L", manager=manager, id=4)
        manager.add_tank(computer_tank3)

        self.wn.listen()
        self.wn.onkeypress(user_tank.move_up, "Up")
        self.wn.onkeypress(user_tank.move_down, 'Down')
        self.wn.onkeypress(user_tank.move_right, 'Right')
        self.wn.onkeypress(user_tank.move_left, 'Left')
        self.wn.onkeypress(user_tank.rotate_right, 'e')
        self.wn.onkeypress(user_tank.rotate_left, 'q')
        self.wn.onkeypress(user_tank.aim_bot, 'a')

        i = 0
        while True:
            self.wn.update()
            if not i % 250:
                manager.spy(user_tank)
            i+=1

g = Game()
g.start()