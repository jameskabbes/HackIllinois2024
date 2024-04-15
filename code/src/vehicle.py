from typing import TypedDict
from . import motor
from . import wheel_encoder
import numpy as np

Heading = float  # in radians


class MotorsConfig(TypedDict):
    left: motor.Config
    right: motor.Config


class Config(TypedDict):
    motors: MotorsConfig


class Vehicle:

    left_motor: motor.Motor
    right_motor: motor.Motor
    mode: str | None
    current_speed: motor.Speed
    current_heading: Heading
    slant: float
    heading_history: list[Heading, tuple[
        wheel_encoder.Ticks, wheel_encoder.Ticks]]
    MAX_LEN_HEADING_HISTORY: int = 20

    FORWARD_HEADING = 0.0
    PIVOT_LEFT_HEADING = np.pi / 2
    PIVOT_RIGHT_HEADING = -np.pi / 2
    BACKWARD_HEADING = np.pi

    def __init__(self, config: Config):

        self.left_motor = motor.Motor(config['motors']['left'])
        self.right_motor = motor.Motor(config['motors']['right'])
        self.current_speed = 0.0
        self.current_heading = 0.0

        self.slant = 0.0  # negative means it slants left, positive means it slants right
        self.heading_history = []

    def drive(self):

        self.calculate_slant()
        pass

    def calculate_slant(self):
        """process the slant given the last N speed logs"""

        if len(self.slant_history) > Vehicle.LENGTH_SLANT_HISTORY:
            del self.slant_history[: len(
                self.slant_history) - Vehicle.LENGTH_SLANT_HISTORY]

        for i in range(len(self.slant_history) - 1):
            pass

    def stop(self) -> None:
        """stop both motors"""
        self.left_motor.stop()
        self.right_motor.stop()

    def drive_forward(self, speed: float = 1.0) -> None:
        """turn both motors forward at a given speed"""
        self.mode = 'forward'
        self.drive(speed, True, speed, True)

    def drive_backward(self, speed: float = 1.0) -> None:
        """turn both motors backward at a given speed"""
        self.mode = 'backward'
        self.drive(speed, False, speed, False)

    def pivot_left(self, speed: float = 1.0) -> None:
        """at the same speed, drive the left motor backward, and the right motor forward"""
        self.drive(speed, False, speed, True)

    def pivot_right(self, speed: float = 1.0) -> None:
        """at the same speed, drive the left motor forward, and the right motor backward"""
        self.drive(speed, True, speed, False)

    def drive(self, left_speed: float, left_direction: bool, right_speed: float, right_direction: bool):

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

    def _motor_control(self, speed: motor.Speed, heading: Heading) -> None:
        """control the each motor's speed and direction without any slant correction"""

        bounded_heading = heading % (2*np.pi)

        # turning left
        if heading < (np.pi/2):

        self.left_motor.drive(left_speed, left_direction)
        self.right_motor.drive(right_speed, right_direction)

    def _raw_motor_control(self, left_speed: motor.Speed, left_direction: motor.Direction, right_speed: motor.Speed, right_direction: motor.Direction):

        pass
