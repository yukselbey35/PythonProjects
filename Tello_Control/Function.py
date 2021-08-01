from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())
me.takeoff()

def movefourdirection():
    me.move_forward(30)
    sleep(2)
    me.move_back(30)
    sleep(2)
    me.send_rc_control(50,0,0,0)
    sleep(3)
    me.send_rc_control(-50,0,0,0)
    sleep(2)
    me.send_rc_control(0,0,0,0)
    sleep(1)

def flyup():
    me.send_rc_control(0, 0, 20, 0)
    sleep(2)
def flyxyz():
    me.send_rc_control(30, 30, 30, 30)
    sleep(2)
    me.send_rc_control(-30, -30, -30, -30)
    sleep(2)
for i in range(2):
    movefourdirection()
    flyup()
    me.flip_left()
    me.flip_right()
    me.send_rc_control(0,0,0,0)
    sleep(1)
me.flip_forward()
sleep(1)

me.flip_back()
flyxyz()
me.send_rc_control(0,0,0,0)
sleep(3)

me.land()