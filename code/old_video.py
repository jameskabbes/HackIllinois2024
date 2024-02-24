from src import camera as camera_module
from src import led as led_module
from src import motor as motor_module
from src import motor_rotations

import time



class ModelType(Enum): 
    YOLOv8n = 'yolov8n.pt'     
    YOLOv8s = 'yolov8s.pt' 
    YOLOv8x = 'yolov8x.pt' 

def detectPersonInFrame(frame, modelType: ModelType):
    model = YOLO(modelType.value)
    results = model(frame)
    person_detected = any(cls == 0 for cls in results[0].boxes.cls)
    if person_detected:
        return 1
    else:
        return 0

if __name__ == '__main__':
    total_seconds = 3
    cycle_time = 3

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

    while True:
        left_motor.forward(1)
        right_motor.forward(0.6)
        camera.capture()
        image_array = camera.image_array
        #ret, frame = cap.read()
        #cap.release()
        #cv2.destroyAllWindows()
        condition = detectPersonInFrame(image_array[:, :, :3], ModelType.YOLOv8n)
        print(condition)
        if(condition == 1):
            left_motor.stop()
            right_motor.stop()
            print('ON!')
            led1.on()
            led2.on()
            time.sleep(cycle_time)
            led1.off()
            led2.off()