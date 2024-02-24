from typing import TypedDict
from gpiozero import Button


class Config(TypedDict):
    pin: int


class Switch(Button):

    state: bool

    """child class of gpiozero.Button"""

    def __init__(self, config: Config):
        super().__init__(config['pin'])
        self.state = False
        self.when_released = self.switch_state

    def switch_state(self):
        self.state = not self.state
