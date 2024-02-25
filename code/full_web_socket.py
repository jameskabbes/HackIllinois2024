from src import motor as motor_module
from src import motor_rotations
from src import led as led_module
import time
from video import detectPersonInFrame, ModelType
from src import distance_sensor as distance_sensor_module
from src import camera as camera_module
from src import switch as switch_module
import paho.mqtt.client as mqtt
import json

MOTOR_OFFSET = 1
DT = 0.1
DISTANCE_RANGE = 0.7
SQUARE_SIZE = 8

#first we need to start the timer at the start of the program
#the normal behaviour is that the robot will move forward for 10 seconds and then take a 90 degree turn and it will keep doing this so it moves in a square
#however, if the distance sensors give a reading of less than 1 meter and more than 0 meters, the robot will stop and take a 90 degree turn towards the direction of the sensor that gave the reading
#it will then check if there is a person in the frame, if there is, it will stop and turn on the leds, if there isn't, it will turn back to the original direction and continue moving in the square
#the robot will keep doing this until the program is stopped
#remeber that when an interrupt happens, the robot needs to remember at what time it stopped and then continue from that point when the program is started again to ensure it moves for 10 seconds and then takes a 90 degree turn
#the robot will also need to remember the direction it was moving in when the interrupt happened and then continue moving in that direction when the program is started again

def move_in_square():
    global start_time
    pic_time = 0
    while True:
        while time.time() - start_time < SQUARE_SIZE:

            distance1 = distance_sensor1.distance
            distance2 = distance_sensor2.distance

            if 0 < distance1 < DISTANCE_RANGE or 0 < distance2 < DISTANCE_RANGE:
                led1.on() #detected something and now we will turn towards it
                temp_start_time = time.time()
                handle_obstacle(distance1, distance2)
                start_time += (time.time() - temp_start_time)
            
            led1.off()
            motor_rotations.move_forward(left_motor, right_motor, 1, s1=1, s2=1)
            time.sleep(DT)
        
            temp_start_time = time.time()
            camera.capture()
            if pic_time%4 == 0:
                image_array = camera.image_array
                person_detected = detectPersonInFrame(image_array[::-1, :, :3], ModelType.YOLOv8n)
                start_time += (time.time() - temp_start_time)

            if person_detected == 1:
                led1.on()
                led2.on()
                time.sleep(2)
                led1.off()
                led2.off()
                start_time+=2

            person_detected = 0
            pic_time += 1
        
        led2.on()
        motor_rotations.rotate_cw_90_deg(left_motor, right_motor)
        start_time = time.time()
        time.sleep(0.5)
        led2.off()

def move_in_line():
    global start_time
    pic_time = 0
    while True:
        while time.time() - start_time < SQUARE_SIZE:

            distance1 = distance_sensor1.distance
            distance2 = distance_sensor2.distance

            if 0 < distance1 < DISTANCE_RANGE or 0 < distance2 < DISTANCE_RANGE:
                led1.on() #detected something and now we will turn towards it
                temp_start_time = time.time()
                handle_obstacle(distance1, distance2)
                start_time += (time.time() - temp_start_time)
            
            led1.off()
            motor_rotations.move_forward(left_motor, right_motor, 1, s1=1, s2=1)
            time.sleep(DT)
        
            temp_start_time = time.time()
            camera.capture()
            if pic_time%4 == 0:
                image_array = camera.image_array
                person_detected = detectPersonInFrame(image_array[::-1, :, :3], ModelType.YOLOv8n)
                start_time += (time.time() - temp_start_time)

            if person_detected == 1:
                led1.on()
                led2.on()
                time.sleep(2)
                led1.off()
                led2.off()
                start_time+=2

            person_detected = 0
            pic_time += 1
        
        led2.on()
        motor_rotations.rotate_cw_90_deg(left_motor, right_motor)
        time.sleep(0.5)
        motor_rotations.rotate_cw_90_deg(left_motor, right_motor)
        start_time = time.time()
        time.sleep(0.5)
        led2.off()

def move_in_triangle():
    global start_time
    pic_time = 0
    while True:
        while time.time() - start_time < SQUARE_SIZE:

            distance1 = distance_sensor1.distance
            distance2 = distance_sensor2.distance

            if 0 < distance1 < DISTANCE_RANGE or 0 < distance2 < DISTANCE_RANGE:
                led1.on() #detected something and now we will turn towards it
                temp_start_time = time.time()
                handle_obstacle(distance1, distance2)
                start_time += (time.time() - temp_start_time)
            
            led1.off()
            motor_rotations.move_forward(left_motor, right_motor, 1, s1=1, s2=1)
            time.sleep(DT)
        
            temp_start_time = time.time()
            camera.capture()
            if pic_time%4 == 0:
                image_array = camera.image_array
                person_detected = detectPersonInFrame(image_array[::-1, :, :3], ModelType.YOLOv8n)
                start_time += (time.time() - temp_start_time)

            if person_detected == 1:
                led1.on()
                led2.on()
                time.sleep(2)
                led1.off()
                led2.off()
                start_time+=2

            person_detected = 0
            pic_time += 1
        
        led2.on()
        motor_rotations.rotate_cw_120_deg(left_motor, right_motor)
        start_time = time.time()
        time.sleep(0.5)
        led2.off()


def stop():
    left_motor.stop()
    right_motor.stop()

def handle_obstacle(distance1, distance2):
    priority_distance = min(distance1, distance2)
    if distance1 == priority_distance:
        motor_rotations.rotate_ccw_90_deg(left_motor, right_motor)
    else:
         motor_rotations.rotate_cw_90_deg(left_motor, right_motor)

    camera.capture()
    image_array = camera.image_array
    person_detected = detectPersonInFrame(image_array[::-1, :, :3], ModelType.YOLOv8n)
    if person_detected:
        # led1.on()
        led2.on()
        time.sleep(1)
        if distance1 == priority_distance:
            motor_rotations.move_forward(left_motor, right_motor, 1, s1=1, s2=1*MOTOR_OFFSET)
            #time.sleep(3)
            motor_rotations.move_backward(left_motor, right_motor, 1, s1=1, s2=1*MOTOR_OFFSET)
            motor_rotations.rotate_cw_90_deg(left_motor, right_motor)
            
            
        else:
            motor_rotations.move_forward(left_motor, right_motor, 1, s1=1, s2=1*MOTOR_OFFSET)
            #time.sleep(3)
            motor_rotations.move_backward(left_motor, right_motor, 1, s1=1, s2=1*MOTOR_OFFSET)
            motor_rotations.rotate_ccw_90_deg(left_motor, right_motor)
           
            
        
        # led1.off()
        led2.off()
    else:
        if distance1 == priority_distance:
            motor_rotations.rotate_cw_90_deg(left_motor, right_motor)
        else:
            motor_rotations.rotate_ccw_90_deg(left_motor, right_motor)

    
if __name__ == '__main__':

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

    switch1 = switch_module.Switch({
        "pin": 2
    })

    switch2 = switch_module.Switch({
        "pin": 3
    })

    num_b2_press = 0

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            # Subscribe to the desired topic
            client.subscribe("BotPatrol")
        else:
            print("Failed to connect, return code: ", rc)

    def on_message(client, userdata, msg):
        global num_b2_press
        print("Topic:", msg.topic)
        print("Payload:", msg.payload.decode())

        js = msg.payload.decode().split("\"")

        arg = js[3]
        print("arg: ", arg)

        match arg:
            case "square":
                num_b2_press = 0
            case "triangle":
                num_b2_press = 2
            case "line":
                num_b2_press = 1


        client.disconnect()
        client.loop_stop()

    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_message = on_message

    broker_address = "192.168.0.101"
    broker_port = 1883
    client.connect(broker_address, broker_port)
    client.loop_forever()
    
    led1.on()
    led2.on()
    time.sleep(2)

    match num_b2_press%3:
        case 0:
            led1.off()
            led2.off()
        case 1:
            led1.off()
            led2.on()
        case 2:
            led1.on()
            led2.off()

    temp_start = time.time()

    while time.time()-temp_start < 5:
        time.sleep(1)
    
    led1.off()
    led2.off()

    start_time = time.time()

    match num_b2_press%3:
        case 0:
            move_in_square()
        case 1:
            move_in_line()
        case 2:
            move_in_triangle()
