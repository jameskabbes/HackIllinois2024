from src import params, vehicle as vehicle_module
import json
from pathlib import Path


# read from config.json
config = json.loads(params.CONFIG_PATH.read_text())

# Load Vehicle
vehicle_config = config['vehicle']
vehicle = vehicle_module.Vehicle(vehicle_config)

vehicle.test_run_calculate_slant()
params.SAVED_SLANT_PATH.write_text(str(vehicle.slant))
