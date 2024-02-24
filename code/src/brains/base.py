from typing import TypedDict
from .. import vehicle as vehicle_module, camera as camera_module, distance_sensor as distance_sensor_module, led as led_module, switch as switch_module
import time


class Config(TypedDict):
    sample_hz: int


class Brain:

    """The base Brain object, which all other Brains should inherit"""

    camera: camera_module.Camera
    vehicle: vehicle_module.Vehicle
    distance_sensors: list[distance_sensor_module.DistanceSensor]
    running: bool
    switches: list[switch_module.Switch]
    leds: list[led_module.LED]
    sample_hz: int
    loop_counter: int

    def __init__(self, config: Config,
                 camera: camera_module.Camera,
                 distance_sensors: list[distance_sensor_module.DistanceSensor],
                 leds: list[led_module.LED],
                 switches: list[switch_module.Switch],
                 vehicle: vehicle_module.Vehicle,
                 ):

        self.camera = camera
        self.distance_sensors = distance_sensors
        self.leds = leds
        self.switches = switches
        self.vehicle = vehicle

        self.running = True
        self.sample_hz = config['sample_hz']
        self.loop_counter = 0

    def logic(self):
        """Process sensor data, tell the vehicle how to drive"""
        pass

    def run(self):
        """The main loop of the Brain class. While running, and the switch is one, gather data from sensors and perform brain logic"""

        while self.running:
            start_loop_time = time.time()

            self.camera.capture()
            self.logic()

            # ensure that the loop is running at the correct max frequency
            time.sleep(max(0, 1/self.sample_hz -
                       (time.time() - start_loop_time)))

            self.loop_counter += 1
