from src import wheel_encoder
import time
import RPi.GPIO as GPIO


if __name__ == '__main__':

    total_seconds = 60
    start_time = time.time()

    left_encoder = wheel_encoder.WheelEncoder(14)
    right_encoder = wheel_encoder.WheelEncoder(4)

    try:
        while time.time() - start_time > total_seconds:
            start_loop_time = time.time()
            print('Left Ticks: ', left_encoder.ticks)
            print('Right Ticks: ', right_encoder.ticks)
            time.sleep(1)

    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
