from pylx16a.lx16a import *

LX16A.initialize("/dev/ttyUSB0", 0.1)

try:
    servo1 = LX16A(1)
    servo1.set_angle_limits(0, 240)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()
    
servo1.move(120)