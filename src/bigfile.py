import os
import math
import random
import turtle

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

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Sprites:
    def __init__(self, team, direction):
        self.up_node = None
        self.left_node = None
        self.right_node = None
        self.down_node = None

        self.curr_node = self.__generate_list(team, direction)

    def get_curr_sprite(self):
        return self.curr_node.val

    def get_next_sprite(self):
        self.curr_node = self.curr_node.next
        return self.get_curr_sprite()

    def get_prev_sprite(self):
        self.curr_node = self.curr_node.prev
        return self.get_curr_sprite()

    def get_up_sprite(self):
        self.curr_node = self.up_node
        return self.get_curr_sprite()

    def get_down_sprite(self):
        self.curr_node = self.down_node
        return self.get_curr_sprite()

    def get_right_sprite(self):
        self.curr_node = self.right_node
        return self.get_curr_sprite()

    def get_left_sprite(self):
        self.curr_node = self.left_node
        return self.get_curr_sprite()

    def __generate_list(self, team, direction):
        front_node = Node(get_filename(f"../Assets/{team}/tank.gif"))
        right_node = Node(get_filename(f"../Assets/{team}/tankright.gif"))
        left_node = Node(get_filename(f"../Assets/{team}/tankleft.gif"))
        down_node = Node(get_filename(f"../Assets/{team}/tankdown.gif"))

        front_node.next = right_node
        front_node.prev = left_node

        right_node.next = down_node
        right_node.prev = front_node

        down_node.next = left_node
        down_node.prev = right_node

        left_node.next = front_node
        left_node.prev = down_node

        self.up_node = front_node
        self.right_node = right_node
        self.left_node = left_node
        self.down_node = down_node
        
        if not direction or direction == "U":
            return front_node
        elif direction == "R":
            return right_node
        elif direction == "D":
            return down_node
        else:
            return left_node

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

class TankManager:
    def __init__(self):
        self.tanks = []

    def add_tank(self, tank):
        self.tanks.append(tank)

    def spy(self, tank):
        s = ""
        for t in self.tanks:
            if t != tank:
                distance = get_distance(tank, t)
                angle = get_angle(tank, t)
                temp_s = f"Distance: {distance}, Angle: {angle} \n"
                s += temp_s
        print(s)

    def get_closest_tank(self, tank):
        merge_sort(self.tanks, tank)
        return self.tanks[1] # return index 1 to skip the user tank

def get_filename(relpath):
    dir = os.path.dirname(__file__)
    return os.path.join(dir, relpath)

def get_distance(tank, tank1):
    return math.sqrt((tank1.xcor()-tank.xcor())**2 + (tank1.ycor()- tank.ycor())**2)

def get_angle(tank, tank1):
    try:
        return math.degrees(math.asin(abs(tank1.ycor() - tank.ycor())/(abs(get_distance(tank,tank1)))))
    except:
        return 0

def merge_sort(tank_arr, tank):
    if len(tank_arr) > 1:
            mid = len(tank_arr) // 2
            left_half = tank_arr[:mid]
            right_half = tank_arr[mid:]

            merge_sort(left_half, tank)
            merge_sort(right_half, tank)

            i = 0
            j = 0
            k = 0
            while i < len(left_half) and j < len(right_half):
                if get_distance(left_half[i], tank) <= get_distance(right_half[j], tank):
                    tank_arr[k] = left_half[i]
                    i+=1
                else:
                    tank_arr[k] = right_half[j]
                    j+=1
                k+=1

            while i < len(left_half):
                tank_arr[k] = left_half[i]
                i+=1
                k+=1

            while j < len(right_half):
                tank_arr[k] = right_half[j]
                j+=1
                k+=1

def get_random_position(bounds):
    x_bounds = bounds[0]
    y_bounds = bounds[1]

    random_x = random.randint(-x_bounds, x_bounds)
    random_y = random.randint(-y_bounds, y_bounds)

    return random_x, random_y


game = Game()
game.start()