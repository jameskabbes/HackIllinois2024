import RPi.GPIO as GPIO


class WheelEncoder:

    ticks: int
    pin: int

    TICKS_PER_REVOLUTION: int = 192

    def __init__(self, pin: int):

        self.ticks = 0
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.pin, GPIO.RISING,
                              callback=self.rising_callback)

    def rising_callback(self):
        self.ticks += 1

    @property
    def revolutions(self):
        return self.ticks / WheelEncoder.TICKS_PER_REVOLUTION
