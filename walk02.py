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

#angle = int(input("Enter desired motor angle for servo: "))
#print(angle)

time.sleep(1)
print("HERE WE GO!!!")

home1 = 112
home4 = 108
start1 = 90
start4 = 90

atAngle1 = servo1.get_last_instant_move_hw()[0]
atAngle4 = servo4.get_last_instant_move_hw()[0]

temp = atAngle1

while temp < start1:
    servo1.move(temp)
    temp += .5
    time.sleep(.025)
    
while temp > start1:
    servo1.move(temp)
    temp -= .5
    time.sleep(.025)
    
temp = atAngle4
    
while temp < start4:
    servo4.move(temp)
    temp += .5
    time.sleep(.025)
    
while temp > start4:
    servo4.move(temp)
    temp -= .5
    time.sleep(.025)

t = 0

while True:
    deg = 120 - 30 * math.cos(t*2*math.pi/120)
    servo1.move(deg)
    servo4.move(deg)
    time.sleep(.025)
    t += 1