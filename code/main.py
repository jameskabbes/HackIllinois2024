from typing import TypedDict
from src import params, vehicle as vehicle_module, camera as camera_module, distance_sensor as distance_sensor_module, led as led_module, switch as switch_module
from src.brains import ModuleTypes as BrainModuleTypes, Types as BrainTypes
import json


class Config(TypedDict):
    brains: BrainModuleTypes
    camera: camera_module.Config
    distance_sensors: list[distance_sensor_module.Config]
    leds: list[led_module.LED]
    switches: list[switch_module.Switch]
    vehicle: vehicle_module.Config


# read from config.json
config: Config = json.loads(params.CONFIG_PATH.read_text())

# Load Camera
camera_config = config['camera']
camera = camera_module.Camera(camera_config)

# Load Distance Sensors
distance_sensors_config = config['distance_sensors']
distance_sensors: list[distance_sensor_module.DistanceSensor] = []
for d in distance_sensors_config:
    distance_sensors.append(distance_sensor_module.DistanceSensor(d))

# Load LEDs
leds_config = config['leds']
leds: list[led_module.LED] = []
for d in leds_config:
    leds.append(led_module.LED(d))

# Load Switches
switches_config = config['switches']
switches: list[switch_module.Switch] = []
for d in switches_config:
    switches.append(switch_module.Switch(d))

# Load Vehicle
vehicle_config = config['vehicle']
vehicle = vehicle_module.Vehicle(vehicle_config)

# Load Brain
brain_type = 'human_driver'

# merge the base brain config with the brain-specific config, giving priority to the brain-specific config
brain_config = {**config['brains']['base'], **config['brains'][brain_type]}
brain_module = BrainTypes[brain_type]

# initialize a brain instance from whichever brain module you loaded
brain = brain_module.Brain(
    brain_config, camera, distance_sensors, leds, switches, vehicle)

# Tell the brain to drive the vehicle
brain.run()
