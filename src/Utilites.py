import os
import math

def get_filename(relpath):
    dir = os.path.dirname(__file__)
    return os.path.join(dir, relpath)

def get_distance(tank, tank1):
    return math.sqrt((tank1.xcor()-tank.xcor())**2 + (tank1.ycor()- tank.ycor())**2)