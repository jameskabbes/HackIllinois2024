from typing import TypedDict
from . import motor
from . import wheel_encoder
import numpy as np
import time

Slant = float


class MotorsConfig(TypedDict):
    left: motor.Config
    right: motor.Config


class Config(TypedDict):
    motors: MotorsConfig
    slant: Slant


class Vehicle:

    left_motor: motor.Motor
    right_motor: motor.Motor
    mode: str | None
    current_speed: motor.Speed
    slant: Slant  # negative means it slants left, positive means it slants right

    def __init__(self, config: Config):

        self.left_motor = motor.Motor(config['motors']['left'])
        self.right_motor = motor.Motor(config['motors']['right'])
        self.slant = config['slant']

    def stop(self) -> None:
        """stop both motors"""
        self.left_motor.stop()
        self.right_motor.stop()

    def drive_forward(self, speed: motor.Speed = 1.0) -> None:
        """turn both motors forward at a given speed"""
        self.drive(speed, True, speed, True)

    def drive_backward(self, speed: motor.Speed = 1.0) -> None:
        """turn both motors backward at a given speed"""
        self.drive(speed, False, speed, False)

    def pivot_left(self, speed: motor.Speed = 1.0) -> None:
        """at the same speed, drive the left motor backward, and the right motor forward"""
        self.drive(speed, False, speed, True)

    def pivot_right(self, speed: motor.Speed = 1.0) -> None:
        """at the same speed, drive the left motor forward, and the right motor backward"""
        self.drive(speed, True, speed, False)

    def drive(self, left_speed: motor.Speed, left_direction: motor.Direction, right_speed: motor.Speed, right_direction: motor.Direction):

        left_speed, right_speed = self._get_slant_corrected_speeds(
            left_speed, right_speed)

        self._raw_motor_control(
            left_speed, left_direction, right_speed, right_direction)

    def _get_slant_corrected_speeds(self, left_speed: float, right_speed: float) -> tuple[float, float]:

        # vehicle veers left, slow down the right motor proportionally
        if self.slant < 0:
            right_speed *= (1-abs(self.slant))

        # vehicle veers right, slow down the left motor proportionally
        elif self.slant > 0:
            left_speed *= (1-abs(self.slant))

        return (left_speed, right_speed)

    def _raw_motor_control(self, left_speed: motor.Speed, left_direction: motor.Direction, right_speed: motor.Speed, right_direction: motor.Direction) -> None:
        """control the each motor's speed and direction without any slant correction"""

        self.left_motor.drive(left_speed, left_direction)
        self.right_motor.drive(right_speed, right_direction)

    def test_run_calculate_slant(self):

        self.left_motor.encoder.ticks = 0
        self.right_motor.encoder.ticks = 0

        self.drive_forward(1.0)
        time.sleep(10)
        self.stop()
        time.sleep(1)

        print('---Left Motor---')
        print('Ticks: ', self.left_motor.encoder.ticks)
        print('Revolutions: ', wheel_encoder.WheelEncoder.revolutions_from_ticks(
            self.left_motor.encoder.ticks))
        print('Distance: ', wheel_encoder.WheelEncoder.distance_from_ticks(
            self.left_motor.encoder.ticks))
        print()

        print('---Right Motor---')
        print('Ticks: ', self.right_motor.encoder.ticks)
        print('Revolutions: ', wheel_encoder.WheelEncoder.revolutions_from_ticks(
            self.right_motor.encoder.ticks))
        print('Distance: ', wheel_encoder.WheelEncoder.distance_from_ticks(
            self.right_motor.encoder.ticks))
        print()

        self.slant = Vehicle.calculate_slant_from_ticks(
            self.left_motor.encoder.ticks, self.right_motor.encoder.ticks)

        print('Vehicle Slant: ', self.slant)

    @staticmethod
    def calculate_slant_from_ticks(left_motor_ticks: wheel_encoder.Ticks, right_motor_ticks: wheel_encoder.Ticks) -> Slant:
        """Calculate the slant of the vehicle based on the difference in ticks between the left and right motors"""

        # if the ticks are the same, the vehicle is not slanted
        if left_motor_ticks == right_motor_ticks:
            return 0.0

        # if the left motor has more ticks than the right motor, the vehicle is slanted left
        elif left_motor_ticks > right_motor_ticks:
            return -1 * (1 - (right_motor_ticks / left_motor_ticks))

        # if the right motor has more ticks than the left motor, the vehicle is slanted right
        elif right_motor_ticks > left_motor_ticks:
            return 1 * (1 - (left_motor_ticks / right_motor_ticks))
