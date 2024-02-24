def move_in_square():
    global start_time
    moving_forward = True
    direction = 0  # 0: forward, 1: right, 2: backward, 3: left
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        # Check sensor readings
        distance1 = distance_sensor1.get_distance()
        distance2 = distance_sensor2.get_distance()

        # Check if distance is within the specified range
        if 0 < distance1 < 1 or 0 < distance2 < 1:
            handle_obstacle(distance1, distance2)
            continue

        # Move forward for 10 seconds, then turn
        if moving_forward and elapsed_time < 10:
            move_forward()
        elif moving_forward and elapsed_time >= 10:
            turn_90_degrees(direction)
            direction = (direction + 1) % 4  # Update direction
            moving_forward = False
            start_time = time.time()  # Reset timer for stationary period
        else:
            # Wait a bit before moving forward again
            if elapsed_time >= 2:
                moving_forward = True
                start_time = time.time()

def move_forward():
    left_motor.forward()
    right_motor.forward()

def turn_90_degrees(direction):
    # Implement turning logic here
    # This is a placeholder function
    stop()  # First, stop the robot
    # Depending on the direction, control the motors to turn 90 degrees
    # Then, reset `start_time` to ensure we move forward for 10 seconds again

def stop():
    left_motor.stop()
    right_motor.stop()

def handle_obstacle(distance1, distance2):
    stop()
    if distance1 < 1:
        pass
        # Turn towards sensor 1
    elif distance2 < 1:
        pass
        # Turn towards sensor 2
    # Capture an image and check for a person
    camera.capture()
    image_array = camera.image_array
    person_detected = detectPersonInFrame(image_array[:, :, :3], ModelType.YOLOv8n)
    if person_detected:
        led1.turn_on()
        led2.turn_on()
        # Wait or perform some action when a person is detected
    else:
        # Turn back to original direction and continue
        turn_90_degrees(direction)

    
if __name__ == '__main__':
    # cap = cv2.VideoCapture(0)
    # ret, frame = cap.read()
    # cap.release()
    # cv2.destroyAllWindows()

    led1 = led_module.LED({
        "pin": 20
    })

    led2 = led_module.LED({
        "pin": 21
    })
    camera = camera_module.Camera({
        "show_preview": False
    })
    left_motor = motor_module.Motor({
        "pins": {
            "speed": 13,
            "control1": 5,
            "control2": 6
        }
    })

    right_motor = motor_module.Motor({
        "pins": {
            "speed": 12,
            "control1": 7,
            "control2": 8
        },
    })

    distance_sensor1 = distance_sensor_module.DistanceSensor({
        "pins": {
            "echo": 23,
            "trigger": 24
        }
    })

    distance_sensor2 = distance_sensor_module.DistanceSensor({
        "pins": {
            "echo": 17,
            "trigger": 27
        }
    })
    
    start_time = time.time()
    move_in_square()