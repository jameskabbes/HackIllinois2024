from ultralytics import YOLO
from enum import Enum
import cv2

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
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()
    print(detectPersonInFrame(frame, ModelType.YOLOv8n))
