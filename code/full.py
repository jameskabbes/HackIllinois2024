from functools import total_ordering
from gpiozero import Motor, DistanceSensor
from time import sleep
import numpy as np
from src import motor as motor_module
from src import motor_rotations
from src import led as led_module
import time
from video import detectPersonInFrame, ModelType
from src import distance_sensor as distance_sensor_module
import cv2
from src import camera as camera_module


MOTOR_OFFSET = 1
DT = 0.25

#first we need to start the timer at the start of the program
#the normal behaviour is that the robot will move forward for 10 seconds and then take a 90 degree turn and it will keep doing this so it moves in a square
#however, if the distance sensors give a reading of less than 1 meter and more than 0 meters, the robot will stop and take a 90 degree turn towards the direction of the sensor that gave the reading
#it will then check if there is a person in the frame, if there is, it will stop and turn on the leds, if there isn't, it will turn back to the original direction and continue moving in the square
#the robot will keep doing this until the program is stopped
#remeber that when an interrupt happens, the robot needs to remember at what time it stopped and then continue from that point when the program is started again to ensure it moves for 10 seconds and then takes a 90 degree turn
#the robot will also need to remember the direction it was moving in when the interrupt happened and then continue moving in that direction when the program is started again

def move_in_square():
    global start_time
    while True:
        while time.time() - start_time < 10:

            distance1 = distance_sensor1.distance
            distance2 = distance_sensor2.distance

            if 0 < distance1 < 0.2 or 0 < distance2 < 0.2:
                led1.on()
                temp_start_time = time.time()
                handle_obstacle(distance1, distance2)
                start_time -= (time.time() - temp_start_time)
            
            led1.off()
            left_motor.forward(1)
            right_motor.forward(1*MOTOR_OFFSET)
            sleep(DT)
        
        led2.on()
        stop()
        motor_rotations.rotate_cw_90_deg(left_motor, right_motor)
        start_time = time.time()
        sleep(4)
        led2.off()


def stop():
    left_motor.stop()
    right_motor.stop()

def handle_obstacle(distance1, distance2):
    stop()
    priority_distance = min(distance1, distance2)
    if distance1 == priority_distance:
        motor_rotations.rotate_ccw_90_deg(left_motor, right_motor)
    else:
         motor_rotations.rotate_cw_90_deg(left_motor, right_motor)

    camera.capture()
    image_array = camera.image_array
    person_detected = detectPersonInFrame(image_array[:, :, :3], ModelType.YOLOv8n)
    if person_detected:
        # led1.on()
        # led2.on()
        time.sleep(3)
        if distance1 == priority_distance:
            motor_rotations.rotate_cw_90_deg(left_motor, right_motor)
        else:
            motor_rotations.rotate_ccw_90_deg(left_motor, right_motor)
        
        # led1.off()
        # led2.off()
    else:
        if distance1 == priority_distance:
            motor_rotations.rotate_cw_90_deg(left_motor, right_motor)
        else:
            motor_rotations.rotate_ccw_90_deg(left_motor, right_motor)

    
if __name__ == '__main__':

    led1 = led_module.LED({
        "pin": 20
    })

    led2 = led_module.LED({
        "pin": 21
    })
    camera = camera_module.Camera({
        "show_preview": False
    })
    left_motor = motor_module.Motor({
        "pins": {
            "speed": 13,
            "control1": 5,
            "control2": 6
        }
    })

    right_motor = motor_module.Motor({
        "pins": {
            "speed": 12,
            "control1": 7,
            "control2": 8
        },
    })

    distance_sensor1 = distance_sensor_module.DistanceSensor({
        "pins": {
            "echo": 23,
            "trigger": 24
        }
    })

    distance_sensor2 = distance_sensor_module.DistanceSensor({
        "pins": {
            "echo": 17,
            "trigger": 27
        }
    })
    
    start_time = time.time()
    move_in_square()
