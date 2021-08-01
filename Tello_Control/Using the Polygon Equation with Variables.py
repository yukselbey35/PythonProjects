from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())

number_of_sides = 0
leg_distance = 0
interior_angle = 0
exterior_angle = 0
me.takeoff()
"""Making a polygon with variables and formula """
def make_polygon():
    number_of_sides = 5
    leg_distance = 75
    interior_angle = ((number_of_sides - 2) * 180) / number_of_sides
    exterior_angle = 180 - interior_angle

    for i in range(number_of_sides):
        me.move_forward(leg_distance)
        sleep(1)
        me.get_yaw(exterior_angle)
        sleep(1)
make_polygon()
me.land()