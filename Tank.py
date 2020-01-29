import turtle
from Node import Node

class Tank(turtle.Turtle):
    def __init__(self, team):
        super().__init__()
        self.team = team
        self.curr_node = self.__generate_list()

        self.shape(self.curr_node.val)
        self.up()

    def move_up(self):
        if self.ycor() <= 220:
            self.sety(self.ycor()+60)

    def move_down(self):
        if self.ycor() >= -220:
            self.sety(self.ycor()-60)

    def move_left(self):
        if self.xcor() > -350:
            self.setx((self.xcor()-60))

    def move_right(self):
        if self.xcor() <= 350:
            self.setx((self.xcor()+60))

    def rotate_right(self):
        self.curr_node = self.curr_node.next
        self.draw(self.curr_node.val)

    def rotate_left(self):
        self.curr_node = self.curr_node.prev
        self.draw(self.curr_node.val)

    def draw(self, asset):
        self.shape(asset)

    def __generate_list(self):
        frontNode = Node(f"Assets/{self.team}/tank.gif")
        rightNode = Node(f"Assets/{self.team}/tankright.gif")
        leftNode = Node(f"Assets/{self.team}/tankleft.gif")
        downNode = Node(f"Assets/{self.team}/tankdown.gif")

        frontNode.next = rightNode
        frontNode.prev = leftNode

        rightNode.next = downNode
        rightNode.prev = frontNode

        downNode.next = leftNode
        downNode.prev = rightNode

        leftNode.next = frontNode
        leftNode.prev = downNode

        return frontNode