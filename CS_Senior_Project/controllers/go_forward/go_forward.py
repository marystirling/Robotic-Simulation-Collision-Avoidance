"""go_forward controller."""
#!/usr/bin/env python3.8
# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor


def move_forward():
    left_motor.setVelocity(MAX_SPEED);
    right_motor.setVelocity(MAX_SPEED);
# create the Robot instance.
robot = Robot()


# get the time step of the current world.
timestep = 64

MAX_SPEED = 6.28

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
    
left_motor.setPosition(10.0)
right_motor.setPosition(10.0)
    
    
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.
    move_forward()
    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
