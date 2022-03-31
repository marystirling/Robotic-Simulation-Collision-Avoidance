"""my_controller_lidar controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Lidar
import math



def run_robot(robot):
    # get the time step of the current world.
    timestep = 32
    max_speed = 6.28
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  motor = robot.getDevice('motorname')
    #  ds = robot.getDevice('dsname')
    #  ds.enable(timestep)
    
    # Motors
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    
    left_motor.setPosition(20.0)
    right_motor.setPosition(20.0)
    
    
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    
    
  
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        

      
        # Enter here functions to send actuator commands, like:
        #  motor.setPosition(10.0)
        left_motor.setVelocity(max_speed*0.25)
        right_motor.setVelocity(max_speed*0.25)
        
        
        counter = counter + 1

# Enter here exit cleanup code.


if __name__ == "__main__":
# create the Robot instance.
    my_robot = Robot()
    #my_lidar = LidarPoint()
    run_robot(my_robot)