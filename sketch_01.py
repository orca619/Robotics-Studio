from lx16a import *
import time

LX16A.initialize("/dev/ttyUSB0", 0.1)

try:
    servo2 = LX16A(2)
    servo3 = LX16A(3)
    servo2.set_angle_limits(0, 240)
    servo3.set_angle_limits(0, 240)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()
    
x = 0

while True:
    if x % 6 == 0: 
        servo2.move(120)
        time.sleep(1)
    elif x % 6 == 1:
        servo2.move(170)
        time.sleep(1)
    elif x % 6 == 2:
        servo2.move(180)
        time.sleep(1)
    elif x % 6 == 3: 
        servo3.move(120)
        time.sleep(1)
    elif x % 6 == 4:
        servo3.move(170)
        time.sleep(1)
    elif x % 6 == 5:
        servo3.move(180)
        time.sleep(1)
    
    x += 1