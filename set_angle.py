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
    
angle1 = int(input("Enter desired motor angle for servo1: "))
print(angle1)

atAngle1 = servo1.get_last_instant_move_hw()[0]
print(atAngle1)

temp = atAngle1

while temp < angle1:
    servo1.move(temp)
    temp += 1
    time.sleep(.05)
    
while temp > angle1:
    servo1.move(temp)
    temp -= 1
    time.sleep(.05)
    
angle2 = int(input("Enter desired motor angle for servo2: "))
print(angle2)

atAngle2 = servo2.get_last_instant_move_hw()[0]
print(atAngle2)

temp = atAngle2

while temp < angle2:
    servo2.move(temp)
    temp += 1
    time.sleep(.05)
    
while temp > angle2:
    servo2.move(temp)
    temp -= 1
    time.sleep(.05)
    
angle3 = int(input("Enter desired motor angle for servo3: "))
print(angle3)

atAngle3 = servo3.get_last_instant_move_hw()[0]
print(atAngle3)

temp = atAngle3

while temp < angle3:
    servo3.move(temp)
    temp += 1
    time.sleep(.05)
    
while temp > angle3:
    servo3.move(temp)
    temp -= 1
    time.sleep(.05)
    
angle4 = int(input("Enter desired motor angle for servo4: "))
print(angle4)

atAngle4 = servo4.get_last_instant_move_hw()[0]
print(atAngle4)

temp = atAngle4

while temp < angle4:
    servo4.move(temp)
    temp += 1
    time.sleep(.05)
    
while temp > angle4:
    servo4.move(temp)
    temp -= 1
    time.sleep(.05)
    
angle5 = int(input("Enter desired motor angle for servo5: "))
print(angle5)

atAngle5 = servo5.get_last_instant_move_hw()[0]
print(atAngle5)

temp = atAngle5

while temp < angle5:
    servo5.move(temp)
    temp += 1
    time.sleep(.05)
    
while temp > angle5:
    servo5.move(temp)
    temp -= 1
    time.sleep(.05)
    
angle6 = int(input("Enter desired motor angle for servo6: "))
print(angle6)

atAngle6 = servo6.get_last_instant_move_hw()[0]
print(atAngle6)

temp = atAngle6

while temp < angle6:
    servo6.move(temp)
    temp += 1
    time.sleep(.05)
    
while temp > angle6:
    servo6.move(temp)
    temp -= 1
    time.sleep(.05)
    
angle7 = int(input("Enter desired motor angle for servo7: "))
print(angle7)

atAngle7 = servo7.get_last_instant_move_hw()[0]
print(atAngle7)

temp = atAngle7

while temp < angle7:
    servo7.move(temp)
    temp += 1
    time.sleep(.05)
    
while temp > angle7:
    servo7.move(temp)
    temp -= 1
    time.sleep(.05)
    
angle8 = int(input("Enter desired motor angle for servo8: "))
print(angle8)

atAngle8 = servo8.get_last_instant_move_hw()[0]
print(atAngle8)

temp = atAngle8

while temp < angle8:
    servo8.move(temp)
    temp += 1
    time.sleep(.05)
    
while temp > angle8:
    servo8.move(temp)
    temp -= 1
    time.sleep(.05)