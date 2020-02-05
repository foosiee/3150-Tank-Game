from Node import Node
from Utilites import get_filename

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