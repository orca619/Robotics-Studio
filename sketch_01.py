from lx16a import *
import time

LX16A.initialize("/dev/ttyUSB0", 0.1)

try:
    servo1 = LX16A(1)
    servo2 = LX16A(2)
    servo3 = LX16A(3)
    servo4 = LX16A(4)
    servo5 = LX16A(5)
    servo6 = LX16A(6)
    servo7 = LX16A(7)
    servo8 = LX16A(8)
    servo1.set_angle_limits(0, 240)
    servo2.set_angle_limits(0, 240)
    servo3.set_angle_limits(0, 240)
    servo4.set_angle_limits(0, 240)
    servo5.set_angle_limits(0, 240)
    servo6.set_angle_limits(0, 240)
    servo7.set_angle_limits(0, 240)
    servo8.set_angle_limits(0, 240)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()
    
x = 0

while x==0:
    servo1.move(60)
    time.sleep(.5)
    servo2.move(60)
    time.sleep(.5)
    servo3.move(60)
    time.sleep(.5)
    servo4.move(60)
    time.sleep(.5)
    servo5.move(60)
    time.sleep(.5)
    servo6.move(60)
    time.sleep(.5)
    servo7.move(60)
    time.sleep(.5)
    servo8.move(60)
    time.sleep(.5)
    servo1.move(120)
    time.sleep(.5)
    servo2.move(120)
    time.sleep(.5)
    servo3.move(120)
    time.sleep(.5)
    servo4.move(120)
    time.sleep(.5)
    servo5.move(120)
    time.sleep(.5)
    servo6.move(120)
    time.sleep(.5)
    servo7.move(120)
    time.sleep(.5)
    servo8.move(120)
    time.sleep(.5)
    x+=1

# while True:
#     if x % 6 == 0: 
#         servo2.move(120)
#         time.sleep(1)
#     elif x % 6 == 1:
#         servo2.move(170)
#         time.sleep(1)
#     elif x % 6 == 2:
#         servo2.move(180)
#         time.sleep(1)
#     elif x % 6 == 3: 
#         servo3.move(120)
#         time.sleep(1)
#     elif x % 6 == 4:
#         servo3.move(170)
#         time.sleep(1)
#     elif x % 6 == 5:
#         servo3.move(180)
#         time.sleep(1)
    
#     x += 1