from src import wheel_encoder
import time
import RPi.GPIO as GPIO


if __name__ == '__main__':

    total_seconds = 60
    start_time = time.time()

    left_encoder = wheel_encoder.WheelEncoder(14)
    right_encoder = wheel_encoder.WheelEncoder(4)

    print(left_encoder.ticks, right_encoder.ticks)
    time.sleep(10)
    print(left_encoder.ticks, right_encoder.ticks)
