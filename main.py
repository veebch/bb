# A 1-coffee long project that will turn a cheap stepper motor by a defined amount every n to n + m minutes. 
# This is a solution looking for a problem. Proof of concept on Blue Parking Disc that auto-adjusts.
# Purely didactic proof-of-concept and we're not suggesting that you use it to annoy traffic wardens.

import time
import urandom
from machine import Pin

n = 60 # Baseline time (minutes)
m = 15 # Margin of error (minutes)

#flash LED to show that code is running
led = Pin(25, Pin.OUT)

# Turn the LED on
led.value(1)
time.sleep(1)  # Keep it on for 1 second

# Turn the LED off
led.value(0)
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
step_motor(64*8)
# Constants
STEPS_PER_REVOLUTION = 64*8  # 28BYJ-48 64*64/8 steps per revolution
print('Steps per Hour:', STEPS_PER_REVOLUTION // 12)
while True:
    print("looping")
    # Coming back after the baseline iteration minus a little randomly chosen time to spare
    time_to_spare = urandom.randint(0,m)  
    interval_minutes = n - time_to_spare
    interval_seconds = interval_minutes * 60
    correct = (n-time_to_spare)/60
    # steps per h * return time (hours)
    # so if you return early, the clock is already a touch too far ahead, and this needs to be compensated for
    STEPS_TO_TURN = int((STEPS_PER_REVOLUTION / 12)*correct)
    print(STEPS_TO_TURN, 'steps because I returned ', time_to_spare,' mins early. Correction factor:', correct)
    time.sleep(interval_seconds)
    # Move the motor 
    step_motor(STEPS_TO_TURN)



