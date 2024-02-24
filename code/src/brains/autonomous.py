from . import base
import cv2
import numpy as np


class Config(base.Config):
    pass


class Brain(base.Brain):

    """The autonomous Brain object, drives the vehicle autonomously based on information gathered by the sensors"""

    def __init__(self, config: Config, *arg):
        super().__init__(config, *arg)

    def is_obstacle_too_close(image, threshold_area=0.1):
        if image is None:
            raise ValueError("Image is None")
        if image.dtype != 'uint8':
            raise TypeError("Image dtype is not 'uint8'")

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply edge detection or thresholding to identify potential obstacles
        _, thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)

        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Check if any contour is large enough to be considered close
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area / (image.shape[0] * image.shape[1]) > threshold_area:
                return True  # Obstacle is too close
        return False

    """Returns which distance sensors and camera detect obstacles"""
    def detectObstacles(self):
        obstacle_right = self.distance_sensors[1].distance < 0.25
        obstacle_left = self.distance_sensors[0].distance < 0.25

        # image of the camera
        image = self.camera.image_array
        obstacle_front = self.is_obstacle_too_close(image); 

        return obstacle_left, obstacle_right, obstacle_front

    def logic(self):
        """If anything is detected by the distance_sensors, stop the car"""

        # if anything is detected by the sensors, stop the car
        stop = False
        obstacle_left, obstacle_right, obstacle_front = self.detectObstacles()

        if obstacle_right and not obstacle_left: 
            #turn left
            print("LEFT")
            self.vehicle.pivot_left(1)
        elif obstacle_left and not obstacle_right:
            #turn right
            print("RIGHT")
            self.vehicle.pivot_right(1)
        elif obstacle_right and obstacle_left:
            #stop motors
            print("STOP") 
            self.vehicle.stop()
            stop = True

        # for distance_sensor in self.distance_sensors:
        #     if distance_sensor.distance < 0.25:
        #         self.vehicle.stop()
        #         stop = True

        if not stop:
            self.vehicle.drive_forward()
