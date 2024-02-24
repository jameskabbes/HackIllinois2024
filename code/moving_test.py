import numpy as np
from src import motor as motor_module
from src import motor_rotations
from src import led as led_module
import time

MOTOR_OFFSET = 1

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

    speeds = list(np.linspace(0, 1, 11)) + list(np.linspace(0.9, 0, 10))

    dt = 0.25
    left_motor.stop()
    right_motor.stop()
    time.sleep(dt)

    while True:
    # motor_rotations.move_forward(left_motor, right_motor, 2)
    # motor_rotations.rotate_ccw_90_deg(left_motor, right_motor)
    # motor_rotations.rotate_ccw_90_deg(left_motor, right_motor)
    # motor_rotations.move_forward(left_motor, right_motor, 2)
    # motor_rotations.rotate_ccw_90_deg(left_motor, right_motor)
    # motor_rotations.move_forward(left_motor, right_motor, 2)
        try:
            motor_rotations.move_forward(left_motor, right_motor, 2)
            motor_rotations.rotate_cw_90_deg(left_motor, right_motor)
        except KeyboardInterrupt:
            left_motor.stop()
            right_motor.stop()
            exit(0)
