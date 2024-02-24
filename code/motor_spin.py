import numpy as np
from src import motor as motor_module
from src import motor_rotations
import time

if __name__ == '__main__':

    motor1 = motor_module.Motor({
        "pins": {
            "speed": 13,
            "control1": 5,
            "control2": 6
        }
    })

    motor2 = motor_module.Motor({
        "pins": {
            "speed": 12,
            "control1": 7,
            "control2": 8
        }
    })

    speeds = list(np.linspace(0, 1, 11)) + list(np.linspace(0.9, 0, 10))

    dt = 0.25
    motor1.stop()
    motor2.stop()
    time.sleep(dt)

    # for speed in speeds:
    #     print('Motor forward at {}% speed'.format(speed * 100))
    #     motor1.forward(speed)
    #     motor2.forward(speed)
    #     time.sleep(dt)

    # for speed in speeds:
    #     print('Motor backward at {}% speed'.format(speed * 100))
    #     motor1.backward(speed)
    #     motor2.backward(speed)
    #     time.sleep(dt)

    motor_rotations.rotate_ccw_90_deg(motor1, motor2)
    time.sleep(dt)
    motor_rotations.rotate_cw_90_deg(motor1, motor2)
    time.sleep(dt)
    motor_rotations.move_forward(motor1, motor2, 5)
    time.sleep(dt)
    motor_rotations.move_backward(motor1, motor2, 5)
    time.sleep(dt)
