from Utilites import get_distance, get_angle, merge_sort

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

        # closest_tank = None
        # closest_distance = 9999
        # for t in self.tanks:
        #     if t != tank:
        #         distance = get_distance(tank, t)
        #         if distance < closest_distance:
        #             closest_tank = t
        #             closest_distance = distance
        # return closest_tank