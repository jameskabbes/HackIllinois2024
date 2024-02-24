from src import switch as switch_module
import time


if __name__ == '__main__':

    total_seconds = 60
    sample_hz = 2

    switch1 = switch_module.Switch({
        "pin": 2
    })

    switch2 = switch_module.Switch({
        "pin": 3
    })

    start_time = time.time()
    while time.time() - start_time < total_seconds:

        loop_start = time.time()
        print(1, 'Pressed: ', switch1.is_pressed, 'State: ', switch1.state)
        print(2, 'Pressed: ', switch2.is_pressed, 'State: ', switch2.state)

        time.sleep(max(0, 1/sample_hz - (time.time() - loop_start)))
