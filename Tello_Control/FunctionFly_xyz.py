from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())
me.takeoff()

def flyxyz():
    me.send_rc_control(20, 20, 20, 10)
    sleep(2)
    me.send_rc_control(-20, -20, -20, -10)
    sleep(2)
    me.send_rc_control(0, 0, 0, 0)
    sleep(1)

flyxyz()
me.land()