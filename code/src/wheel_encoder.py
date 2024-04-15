import RPi.GPIO as GPIO
from gpiozero import Button


class WheelEncoder(Button):

    ticks: int
    pin: int

    TICKS_PER_REVOLUTION: int = 192

    def __init__(self, pin: int):

        super().__init__(pin=pin, pull_up=True)
        self.when_pressed = self.increment_ticks
        self.ticks = 0
        self.pin = pin

    def increment_ticks(self):
        self.ticks += 1

    @property
    def revolutions(self):
        return self.ticks / WheelEncoder.TICKS_PER_REVOLUTION
