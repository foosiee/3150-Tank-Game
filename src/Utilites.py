import os
import math

def get_filename(relpath):
    dir = os.path.dirname(__file__)
    return os.path.join(dir, relpath)

def get_distance(tank, tank1):
    return math.sqrt((tank1.xcor()-tank.xcor())**2 + (tank1.ycor()- tank.ycor())**2)

def get_angle(tank, tank1):
    return math.degrees(math.asin(abs(tank1.ycor() - tank.ycor())/(abs(get_distance(tank,tank1)))))

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
