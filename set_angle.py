from lx16a import *
import time
import math

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
    
servoNum = input("Enter servo number you wish to set: ")
angle = input("Enter desired motor angle")
    
t = 0

while t <= 2:
    if servoNum == 1:
        deg = 120 + 30 * math.sin(t * math.pi)
        servo1.move(deg)
    elif servoNum == 2:
        deg = 120 + 30 * math.sin(t * math.pi)
        servo2.move(deg)
    elif servoNum == 3:
        deg = 120 + 30 * math.sin(t * math.pi)
        servo3.move(deg)
    elif servoNum == 4:
        deg = 120 + 30 * math.sin(t * math.pi)
        servo4.move(deg)
    elif servoNum == 5:
        deg = 120 + 30 * math.sin(t * math.pi)
        servo5.move(deg)
    elif servoNum == 6:
        deg = 120 + 30 * math.sin(t * math.pi)
        servo6.move(deg)
    elif servoNum == 7:
        deg = 120 + 30 * math.sin(t * math.pi)
        servo7.move(deg)
    elif servoNum == 8:
        deg = 120 + 30 * math.sin(t * math.pi)
        servo8.move(deg)
    else:
        print("ERROR")
        
    t += .01
    time.sleep(.05)