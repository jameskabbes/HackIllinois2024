from . import base


class Config(base.Config):
    pass


class Brain(base.Brain):

    """The autonomous Brain object, drives the vehicle autonomously based on information gathered by the sensors"""

    def __init__(self, config: Config, *arg):
        super().__init__(config, *arg)

    def logic(self):
        """If anything is detected by the distance_sensors, stop the car"""

        # if anything is detected by the sensors, stop the car
        stop = False
        for distance_sensor in self.distance_sensors:
            if distance_sensor.distance < 0.25:
                self.vehicle.stop()
                stop = True

        if not stop:
            self.vehicle.drive_forward()
