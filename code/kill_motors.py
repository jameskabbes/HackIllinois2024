import numpy as np
from src import motor as motor_module
import time

MOTOR_OFFSET = 0.65

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

    dt = 0.25
    left_motor.stop()
    right_motor.stop()
    time.sleep(dt)