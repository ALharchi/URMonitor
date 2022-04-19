from rtde_receive import RTDEReceiveInterface as RTDEReceive
import time
import sys

import socket

ROBOT_IP = "192.168.1.112" # ROBOT IP
FREQUENCY = 50.0  # Frequency in Hertz. You can go up to 500Hz.

rtde_r = RTDEReceive(ROBOT_IP, FREQUENCY)

def toStr(input):
    value = ""
    for i in input:
        value += (str(i)) + "/"
    return value

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

while True:

    robotPos = rtde_r.getActualQ()
    print (robotPos)
    speedFraction = rtde_r.getTargetSpeedFraction()
    print (speedFraction)

    # POTENTIAL DATA MANIPULATION
    sock.sendto(toStr(robotPos).encode(), ("127.0.0.1", 2022))
    
    time.sleep(1)