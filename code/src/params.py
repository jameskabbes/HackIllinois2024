import os
import pathlib


SRC_PATH = pathlib.Path(os.path.abspath(__file__)).parent
CONFIG_PATH = SRC_PATH / 'config.json'
SAVED_SLANT_PATH = SRC_PATH / 'saved_slant.txt'
