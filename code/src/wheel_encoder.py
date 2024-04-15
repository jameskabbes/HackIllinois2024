import RPi.GPIO as GPIO
from gpiozero import Button
import math


class WheelEncoder(Button):

    ticks: int
    pin: int

    TICKS_PER_REVOLUTION: int = 192
    WHEEL_RADIUS: float = 25.0  # mm

    def __init__(self, pin: int):

        super().__init__(pin=pin, pull_up=True)
        self.when_pressed = self.increment_ticks
        self.ticks = 0

    def increment_ticks(self):
        self.ticks += 1

    @staticmethod
    def revolutions_from_ticks(ticks):
        return ticks / WheelEncoder.TICKS_PER_REVOLUTION

    @staticmethod
    def distance_from_ticks(ticks):
        return 2*math.pi*WheelEncoder.WHEEL_RADIUS * WheelEncoder.revolutions_from_ticks(ticks)
