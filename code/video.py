from ultralytics import YOLO 
from enum import Enum

class ModelType(Enum): 
    YOLOv8n = 'yolov8n.pt'     
    YOLOv8s = 'yolov8s.pt' 
    YOLOv8x = 'yolov8x.pt' 

class Camera(Enum): 
    LOGI_1 = '0'
    LAPTOP = '1' 
    LOGI_2 = '2' 

def liveObjDetection(modelType: ModelType):
    model = YOLO(modelType.value)
    model.predict(source=Camera.LOGI_1.value, show=True)

if __name__ == '__main__': 
    liveObjDetection(ModelType.YOLOv8n)
