from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())
me.takeoff()

me.move_forward(30)
sleep(2)
me.move_back(30)
sleep(2)
me.send_rc_control(50,0,0,0)
sleep(2)
me.send_rc_control(-50,0,0,0)
sleep(2)
me.send_rc_control(0,0,0,0)
sleep(2)
me.flip_left()
me.flip_right()
me.send_rc_control(0,0,0,0)
me.land()