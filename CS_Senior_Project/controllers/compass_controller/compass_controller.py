"""gps_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Compass

# create the Robot instance.
robot = Robot()
max_speed = 6.28




# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())


compass = robot.getDevice("compass")
compass.enable(timestep)

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
    
left_motor.setPosition(10.0)
right_motor.setPosition(10.0)
    
    
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)



# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:

    
    
    left_motor.setVelocity(max_speed*0.25)
    right_motor.setVelocity(max_speed*0.25)
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    #print(gps.getCoordinateSystem())
    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
