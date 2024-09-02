# A 1-coffee long project that will turn a cheap stepper motor by a defined amount every n to n + m minutes. 
# This is a solution looking for a problem. Proof of concept on Blue Parking Disc that auto-adjusts.
# Purely didactic proof-of-concept and we're not suggesting you use it for parking.

import time
import urandom
from machine import Pin

n = 1 # Baseline time (minutes)
m = 0 # Margin of error (minutes)

# Define motor pins and steps
IN1 = Pin(21, Pin.OUT)
IN2 = Pin(20, Pin.OUT)
IN3 = Pin(19, Pin.OUT)
IN4 = Pin(18, Pin.OUT)

# Sequence for 28BYJ-48
step_sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

# Stepper motor functions
def set_step(w1, w2, w3, w4):
    IN1.value(w1)
    IN2.value(w2)
    IN3.value(w3)
    IN4.value(w4)

def step_motor(steps):
    for _ in range(steps):
        for step in step_sequence:
            set_step(step[0], step[1], step[2], step[3])
            time.sleep_ms(2)
    set_step(0,0,0,0)

# Constants
STEPS_PER_REVOLUTION = 64*8  # 28BYJ-48 64*64/8 steps per revolutio n

while True:
    print("looping")
    # Coming back after the baseline iteration minus a little randomly chosen time to spare
    time_to_spare = urandom.randint(0,m)  
    interval_minutes = n - time_to_spare
    interval_seconds = interval_minutes * 60
    STEPS_TO_TURN = STEPS_PER_REVOLUTION // ((12*( n - time_to_spare) // 60))
    # Wait
    time.sleep(interval_seconds)
    
    # Move the motor 
    step_motor(STEPS_TO_TURN)


