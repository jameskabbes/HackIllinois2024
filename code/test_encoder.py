import RPi.GPIO as gpio

ENCODER_PIN = 17
tick_count = 0


def encoder_callback(channel):
    global tick_count
    tick_count += 1


def setup_gpio():
    gpio.set_mode(gpio.BCM)
    gpio.setup(ENCODER_PIN, gpio.IN, pull_up_down=gpio.PUD_UP)
    gpio.add_event_detect(ENCODER_PIN, gpio.FALLING, callback=encoder_callback)


if __name__ == '__main__':
    setup_gpio()

    try:
        while True:
            print(f'Tick count: {tick_count}')

    except KeyboardInterrupt:
        print('done')
    finally:
        gpio.cleanup()
