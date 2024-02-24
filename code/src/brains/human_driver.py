import select
import tty
import termios
import sys
from . import base


class Config(base.Config):
    pass


class Brain(base.Brain):

    """The human_driver Brain object, allows for users to control the vehicle with the keyboard. Not autonomous."""

    def __init__(self, config: Config, *arg):
        super().__init__(config, *arg)

        print('Initializing human_driver.Brain')
        print('Use the WASD keys to drive the vehicle, Q key to quit')

    @staticmethod
    def get_input(timeout: float = None) -> str:
        """Get real-time key input from user"""

        filedescriptors = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin)

        ready, _, _ = select.select([sys.stdin], [], [], timeout)

        if sys.stdin in ready:
            key = sys.stdin.read(1)[0]
        else:
            key = None

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, filedescriptors)

        return key

    def logic(self):
        key = Brain.get_input(1/self.sample_hz)

        if key == 'w':
            self.vehicle.drive_forward(1)
        elif key == 'a':
            self.vehicle.pivot_left(1)
        elif key == 's':
            self.vehicle.drive_backward(1)
        elif key == 'd':
            self.vehicle.pivot_right(1)
        elif key == 'q':
            self.running = False
        else:
            self.vehicle.stop()

        # power on the the LED if the corresponding distance sensor detects it
        for i in range(min(len(self.distance_sensors), len(self.leds))):
            if self.distance_sensors[i].distance < 0.25:
                self.leds[i].on()
            else:
                self.leds[i].off()

        if self.loop_counter % 100 == 0:
            print('Loop counter: ', str(self.loop_counter))
            print('IMAGE')
            print(self.camera.image_array)
            print()
            print('Distance Sensors:')
            for i in range(len(self.distance_sensors)):
                print('Distance Sensor {}: {}'.format(
                    i+1, self.distance_sensors[i].distance))
            print()
            print('')
