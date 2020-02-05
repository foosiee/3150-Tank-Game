from Utilites import get_distance

class TankManager:
    def __init__(self):
        self.tanks = []

    def add_tank(self, tank):
        self.tanks.append(tank)

    def spy(self, tank):
        s = ""
        for t in self.tanks:
            if t != tank:
                s += str(get_distance(tank, t)) + " "
        print(s)

    def get_closest_tank(self, tank):
        closest_tank = None
        closest_distance = 9999
        for t in self.tanks:
            if t != tank:
                distance = get_distance(tank, t)
                if distance < closest_distance:
                    closest_tank = t
                    closest_distance = distance
        return closest_tank
        

    