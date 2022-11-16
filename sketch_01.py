from lx16a import *
import time

LX16A.initialize("/dev/ttyUSB0", 0.1)

try:
    servo1 = LX16A(1)
    servo1.set_angle_limits(0, 240)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()
    
x = 0

while True:
    if x % 3 == 0: 
        servo1.move(120)
        time.sleep(1)
    elif x % 3 == 1:
        servo1.move(60)
        time.sleep(1)
    elif x % 3 == 1:
        servo1.move(180)
        time.sleep(1)
    
    x += 1