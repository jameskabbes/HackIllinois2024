import numpy as np
from src import motor as motor_module
import time
from src import led as led_module

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

    led1 = led_module.LED({
        "pin": 20
    })

    led2 = led_module.LED({
        "pin": 21
    })

    dt = 0.25
    left_motor.stop()
    right_motor.stop()
    led1.off()
    led2.off()
    time.sleep(dt)
