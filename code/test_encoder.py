from src import wheel_encoder
import time
import RPi.GPIO as GPIO


if __name__ == '__main__':

    total_seconds = 10
    start_time = time.time()

    left_encoder = wheel_encoder.WheelEncoder({'pin': 14})
    right_encoder = wheel_encoder.WheelEncoder({'pin': 4})

    while time.time() - start_time < total_seconds:
        print('Left Encoder Ticks: ', left_encoder.ticks)
        print('Right Encoder Ticks: ', right_encoder.ticks)

        time.sleep(.1)
