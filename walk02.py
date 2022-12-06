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
home5 = 106
home8 = 112
start1 = home1 + 30
start4 = home4 + 30
start5 = home5 + 30
start8 = home8 + 30

home2 = 126
home6 = 122
start2 = home2
start6 = home6

home3 = 116
home7 = 122
start2 = home3
start6 = home7

atAngle1 = servo1.get_last_instant_move_hw()[0]
atAngle4 = servo4.get_last_instant_move_hw()[0]
atAngle5 = servo5.get_last_instant_move_hw()[0]
atAngle8 = servo8.get_last_instant_move_hw()[0]

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

temp = atAngle5

while temp < start5:
    servo5.move(temp)
    temp += .5
    time.sleep(.025)
    
while temp > start5:
    servo5.move(temp)
    temp -= .5
    time.sleep(.025)
    
temp = atAngle8
    
while temp < start8:
    servo8.move(temp)
    temp += .5
    time.sleep(.025)
    
while temp > start8:
    servo8.move(temp)
    temp -= .5
    time.sleep(.025)

atAngle2 = servo2.get_last_instant_move_hw()[0]
atAngle6 = servo6.get_last_instant_move_hw()[0]
atAngle3 = servo3.get_last_instant_move_hw()[0]
atAngle7 = servo7.get_last_instant_move_hw()[0]

temp = atAngle2

while temp < start2:
    servo2.move(temp)
    temp += .5
    time.sleep(.025)
    
while temp > start2:
    servo2.move(temp)
    temp -= .5
    time.sleep(.025)
    
temp = atAngle6
    
while temp < start6:
    servo6.move(temp)
    temp += .5
    time.sleep(.025)
    
while temp > start6:
    servo6.move(temp)
    temp -= .5
    time.sleep(.025)

temp = atAngle3

while temp < start3:
    servo3.move(temp)
    temp += .5
    time.sleep(.025)
    
while temp > start3:
    servo3.move(temp)
    temp -= .5
    time.sleep(.025)
    
temp = atAngle7
    
while temp < start7:
    servo7.move(temp)
    temp += .5
    time.sleep(.025)
    
while temp > start7:
    servo7.move(temp)
    temp -= .5
    time.sleep(.025)
    
t = 0

while True:
    theta = t * 2 * math.pi / 120
    
    deg1 = home1 + 30 * math.cos(theta)
    deg4 = home4 + 30 * math.cos(theta)
    deg5 = home5 + 30 * math.cos(theta)
    deg8 = home8 + 30 * math.cos(theta)
    
    deg2 = home2 - 90 * math.sin(theta)
    deg6 = home6 + 30 * math.cos(t*2*math.pi/120)
    deg7 = home7 + 30 * math.cos(t*2*math.pi/120)  
    
    servo1.move(deg1)
    servo4.move(deg4)
    servo5.move(deg5)
    servo8.move(deg8)
    
    if math.sin(theta) > 0 and math.cos(theta) > 0:
        deg3 = home3 - 90 * math.sin(theta)
        servo3.move(deg3)
    elif math.sin(theta) < 0 and math.cos(theta) > 0:
        servo2.move(deg2)
    elif math.sin(theta) < 0 and math.cos(theta) < 0:
        deg3 = home3 + 90 * (1 - math.sin(theta))
        servo2.move(deg2)
        servo3.move()
    else:
                   
    time.sleep(.025)
    t += 1