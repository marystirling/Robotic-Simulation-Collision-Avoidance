"""my_controller_lidar controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Lidar
import math

def move_forward(robot, left_motor, right_motor, max_speed):
    #left_motor = robot.getDevice('left wheel motor')
    #right_motor = robot.getDevice('right wheel motor')
    # set the target position of the motors
    left_motor.setPosition(10.0)
    right_motor.setPosition(10.0)
    left_motor.setVelocity(max_speed)
    right_motor.setVelocity(max_speed)
    print("entered move_function")
    #left_motor.setVelocity(max_speed)
    #right_motor.setVelocity(max_speed)
   
   
def turn_left(left_motor, max_speed):
    left_motor.setPosition(17.91)
    left_motor.setVelocity(max_speed)
 
def turn_right(right_motor, max_speed):
    right_motor.setPosition(17.91)
    right_motor.setVelocity(max_speed)

def run_robot(robot):
    # get the time step of the current world.
    
    
    timestep = 64
    max_speed = 6.28 # angular velocity
    
    # Created motor instances
    left_motor = robot.getDevice("left wheel motor")
    right_motor = robot.getDevice("right wheel motor")
    
    #left_motor.setPosition(float('inf'))
    #left_motor.setVelocity(0.0)
    
    #right_motor.setPosition(float('inf'))
    #right_motor.setVelocity(0.0)
    
    start_time = robot.getTime()
        
        
        #left_speed = max_speed
        #right_speed = max_speed
        
    left_motor.setPosition(float('inf'))
    # left_motor.setVelocity(max_speed)
        
        
    start_time = robot.getTime()
    #counter = 0
    
    while start_time <= 5:
            
    #left_motor.setPosition(17.91)
         left_motor.setVelocity(max_speed)
         current_time = robot.getTime()
         print(f"start time is: {start_time}")
         print(f"end time is: {start_time}")
         duration = current_time - start_time
         print(f"total time is: {duration}")
    
    left_motor.setVelocity(0.0)
       
    

    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        pass
       
        #left_speed = max_speed
        #right_speed = max_speed
        
        

        #move_forward(robot, left_motor, right_motor, max_speed)
        #turn_left(left_motor, max_speed)
        #turn_right(right_motor, max_speed)
       
       
        #right_motor.setPosition(17.91)
        
        #right_motor.setVelocity(max_speed)
        
        #move_forward(max_speed, robot)
        #turn_left(left_motor, max_speed)
        #move_forward(left_motor, right_motor, max_speed)
        #turn_right(right_motor, max_speed)

        # set up the motor speeds at 10% of the MAX_SPEED.
        #left_motor.setVelocity(0.1 * max_speed)
        #right_motor.setVelocity(0.1 * max_speed)
        #if point_tuple[1] < 1:
        #    left_motor.setPosition(17.91)
        #    left_motor.setVelocity(max_speed)

        
      
# Enter here exit cleanup code.


if __name__ == "__main__":
# create the Robot instance.
    my_robot = Robot()
    #my_lidar = LidarPoint()
    run_robot(my_robot)