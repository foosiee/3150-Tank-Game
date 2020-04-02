from Utilites import get_distance, get_angle, merge_sort

class TankManager:
    def __init__(self):
        self.__grid = None
        self.tanks = {}

    def add_tank(self, tank):
        self.update_tank_on_grid(tank)

    def set_grid(self, grid):
        self.__grid = grid

    def get_grid(self):
        return self.__grid

    def update_tank_on_grid(self, tank):
        if tank in self.tanks:
            node = self.tanks[tank]
            self.__deactive_node(node)

        node = self.__grid[tank.gridY][tank.gridX]
        self.tanks[tank] = node
        self.__activate_node(node)

    def spy(self, tank):
        s = ""
        for t in self.tanks.keys():
            if t != tank:
                distance = get_distance(tank, t)
                angle = get_angle(tank, t)
                temp_s = f"Distance: {distance}, Angle: {angle} \n"
                s += temp_s
        print(s)

    def get_closest_tank(self, tank):
        tanks = self.tanks.keys()
        merge_sort(tanks, tank)
        return tanks[1] # return index 1 to skip the user tank

    def __deactive_node(self, node):
        node.set_weight(1)
        node.set_is_empty(True)

    def __activate_node(self, node):
        node.set_weight(1000)
        node.set_is_empty(False)

        # closest_tank = None
        # closest_distance = 9999
        # for t in self.tanks:
        #     if t != tank:
        #         distance = get_distance(tank, t)
        #         if distance < closest_distance:
        #             closest_tank = t
        #             closest_distance = distance
        # return closest_tank