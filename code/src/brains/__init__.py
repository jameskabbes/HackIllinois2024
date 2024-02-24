from . import base, human_driver, autonomous
from typing import TypedDict
import types


class ModuleTypes(TypedDict):
    autonomous: types.ModuleType
    base: types.ModuleType
    human_driver: types.ModuleType


Types: ModuleTypes = {
    "autonomous": autonomous,
    "base": base,
    "human_driver": human_driver
}
