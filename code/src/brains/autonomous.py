from . import base


class Config(base.Config):
    pass


class Brain(base.Brain):

    """The autonomous Brain object, drives the vehicle autonomously based on information gathered by the sensors"""

    def __init__(self, config: Config, *arg):
        super().__init__(config, *arg)

    """Returns which distance sensors and camera detect obstacles"""
    def detectObstacles(self):
        obstacle_right = self.distance_sensors[1].distance < 0.25
        obstacle_left = self.distance_sensors[0].distance < 0.25
        obstacle_front = False; 
        return obstacle_left, obstacle_right, obstacle_front

    def logic(self):
        """If anything is detected by the distance_sensors, stop the car"""

        # if anything is detected by the sensors, stop the car
        stop = False
        
        obstacle_left, obstacle_right, obstacle_front = self.detectObstacles()

        if obstacle_right and not obstacle_left: 
            #turn left
            self.vehicle.pivot_left(1)
        elif obstacle_left and not obstacle_right:
            #turn right
            self.vehicle.pivot_right(1)
        elif obstacle_right and obstacle_left:
            #stop motors 
            self.vehicle.stop()
            stop = True

        # for distance_sensor in self.distance_sensors:
        #     if distance_sensor.distance < 0.25:
        #         self.vehicle.stop()
        #         stop = True

        if not stop:
            self.vehicle.drive_forward()
