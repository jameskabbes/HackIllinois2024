import RPi.GPIO as gpio
import time

ENCODER_PIN = 6
tick_count = 0


def encoder_callback(channel):
    global tick_count
    tick_count += 1


def setup_gpio():
    gpio.setmode(gpio.BCM)
    gpio.setup(ENCODER_PIN, gpio.IN, pull_up_down=gpio.PUD_UP)


if __name__ == '__main__':
    setup_gpio()

    try:
        while True:

            print(gpio.input(ENCODER_PIN))
            time.sleep(1)

            print(f'Tick count: {tick_count}')

    except KeyboardInterrupt:
        print('done')
    finally:
        gpio.cleanup()
