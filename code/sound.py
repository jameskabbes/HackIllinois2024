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


MOTOR_OFFSET = 0.65

def capture_camera_frame(camera):
    camera.capture()
    return camera.image_array

if __name__ == '__main__':
    

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

    led1 = led_module.LED({
        "pin": 20
    })

    led2 = led_module.LED({
        "pin": 21
    })

    camera = camera_module.Camera({
        "show_preview": False
    })

    def sound(right, left, frame):
        target_dir = 0
        if ((right == 1 or right == 0) and (left == 1 or left == 0)):
            print("out of bounds")
            #continue movinf forward
            motor_rotations.move_forward(left_motor, right_motor, 1, s1=1, s2=1*MOTOR_OFFSET)
        elif (min(right, left) == right):
            target_dir = right
        else:
            target_dir = -left
        
        if (target_dir < 1 and target_dir > 0):
            motor_rotations.rotate_cw_90_deg(left_motor, right_motor)
            #rotate_clockwise(90) #move 90 towards right
            if (detectPersonInFrame(frame, ModelType.YOLOv8n) == 1):
                left_motor.stop()
                right_motor.stop()
                led1.on()
                led2.on()
                
            else:
                motor_rotations.rotate_ccw_90_deg(left_motor, right_motor)
        elif (-target_dir < 1 and -target_dir > 0):
            motor_rotations.rotate_ccw_90_deg(left_motor, right_motor)
            #rotate_counter_clockwise(90) #move 90 towards left
            if (detectPersonInFrame(frame, ModelType.YOLOv8n) == 1):
                left_motor.stop()
                right_motor.stop()
                led1.on()
                led2.on()
                
            else:
                motor_rotations.rotate_cw_90_deg(left_motor, right_motor)

    while True:
        image_array = capture_camera_frame(camera)
        sound(distance_sensor1.distance, distance_sensor2.distance, image_array[:, :, :3])
        sleep(2)  # Wait for 2 seconds before capturing the next frame

 
    