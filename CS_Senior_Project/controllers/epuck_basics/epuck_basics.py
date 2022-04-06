"""epuck_basics controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor

time_step = 64

# E-puck angular speed in radians/second
MAX_SPEED = 6.28

# speed of robot to spinning in place (in degrees per second)
ANGULAR_SPEED_DEGREES = 278.237392796

start_times = []

# function to stop the motor (set motor velocity to zero)
def stop():
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

# function to set motor velocity to move forward
def move_forward():
    left_motor.setVelocity(MAX_SPEED)
    right_motor.setVelocity(MAX_SPEED)
    
 # function to set motor velocity to rotate right in place
def rotate_right():
    left_motor.setVelocity(MAX_SPEED)
    right_motor.setVelocity(-MAX_SPEED)

# function to set motor velocity to rotate left in place
def rotate_left():
    left_motor.setVelocity(-MAX_SPEED)
    right_motor.setVelocity(MAX_SPEED)

def calculate_rotation_time(degrees):
    return abs(degrees) / ANGULAR_SPEED_DEGREES   

def calculate_start_time():
    return robot.getTime() 


def rotate_left_in_degrees(degrees):
    rotate_left()
    duration = calculate_rotation_time(degrees)
    print(f"duration: {duration}")
    start_times.append(robot.getTime())
    #print("in rotate_left_in_degrees")
    print(f"start time: {start_times[0]}")
    while (robot.getTime() < start_times[0] + duration):
        print(f"current time: {robot.getTime()}")
        robot.step(time_step)
        #rotate_left()
        #rotate_left()
        #print("rotating left")
    stop()

if __name__ == "__main__":
    robot = Robot()
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    #rotate_left_in_degrees(90)
    while robot.step(time_step) != -1:
        #print("entered while loop")
        #move_forward()
        rotate_left_in_degrees(360)
        #rotate_left()

    
