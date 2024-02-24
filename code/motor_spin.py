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
    # fractions = np.linspace(0.5, 2, 2)

    for i in range(5):
        print(i)
        for _ in range(5):
            motor_rotations.move_forward(left_motor, right_motor, i, s1=1, s2=1*MOTOR_OFFSET)

        motor_rotations.rotate_ccw_90_deg(left_motor, right_motor)
        # motor_rotations.move_backward(left_motor, right_motor, 1, s1=1, s2=1*MOTOR_OFFSET)
        time.sleep(dt)

    # led1.on()
    # motor_rotations.rotate_ccw_90_deg(left_motor, right_motor)
    # time.sleep(dt)
    # motor_rotations.rotate_cw_90_deg(left_motor, right_motor)
    # time.sleep(dt)
    # led1.off()
    # led2.on()
    # motor_rotations.move_forward(left_motor, right_motor, 5, s1=1, s2=1*MOTOR_OFFSET)
    # time.sleep(dt)
    # motor_rotations.move_backward(left_motor, right_motor, 5, s1=1, s2=1*MOTOR_OFFSET)
    # time.sleep(dt)
    # led2.off()
