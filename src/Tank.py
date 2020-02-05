import turtle
from Utilites import get_filename
from Node import Node
from TankManager import TankManager

class Tank(turtle.Turtle):
    def __init__(self, team="User", start_pos=(0,0), direction=None, manager=None, id=0):
        super().__init__()
        self.manager = manager
        self.color = 'red' if team == 'Computer' else 'green'
        self.team = team

        self.front_node = None
        self.left_node = None
        self.right_node = None
        self.down_node = None
        self.curr_node = self.__generate_list(direction)

        self.coords = [0,0] # could abstract more lines 10-13
        self.health = 100 #100 = max health 0 = dead
        self.id = id # not sure what conditonal to use yet maybe a uuid
        self.active = True
        self.draw(self.curr_node.val)
        self.up()
        self.goto(start_pos[0], start_pos[1])

    def move_up(self):
        if self.ycor() <= 290:
            self.sety(self.ycor()+60)

    def move_down(self):
        if self.ycor() >= -290:
            self.sety(self.ycor()-60)

    def move_left(self):
        if self.xcor() > -350:
            self.setx((self.xcor()-60))

    def move_right(self):
        if self.xcor() <= 380:
            self.setx((self.xcor()+60))

    def rotate_right(self):
        self.curr_node = self.curr_node.next
        self.draw(self.curr_node.val)

    def rotate_left(self):
        self.curr_node = self.curr_node.prev
        self.draw(self.curr_node.val)

    def draw(self, asset):
        self.shape(asset)

    def aim_bot(self):
        closest_tank = self.manager.get_closest_tank(self)
        diff_x = abs(closest_tank.xcor()) - abs(self.xcor())
        diff_y = abs(closest_tank.ycor()) - abs(self.ycor())

        if diff_x < diff_y:
            self.goto(closest_tank.xcor(),self.ycor())
        else:
            self.goto(self.xcor(), closest_tank.ycor())

        if closest_tank.ycor() < self.ycor():
            self.curr_node = self.down_node
        elif closest_tank.ycor() > self.ycor():
            self.curr_node = self.front_node            
        elif closest_tank.xcor() < self.xcor():
            self.curr_node = self.left_node
        else:
            self.curr_node = self.right_node

        self.draw(self.curr_node.val)


    def __generate_list(self, direction):
        front_node = Node(get_filename(f"../Assets/{self.team}/tank.gif"))
        right_node = Node(get_filename(f"../Assets/{self.team}/tankright.gif"))
        left_node = Node(get_filename(f"../Assets/{self.team}/tankleft.gif"))
        down_node = Node(get_filename(f"../Assets/{self.team}/tankdown.gif"))

        front_node.next = right_node
        front_node.prev = left_node

        right_node.next = down_node
        right_node.prev = front_node

        down_node.next = left_node
        down_node.prev = right_node

        left_node.next = front_node
        left_node.prev = down_node

        self.front_node = front_node
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