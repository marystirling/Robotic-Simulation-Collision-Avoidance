"""my_controller_lidar controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Lidar
from controller import LidarPoint



def run_robot(robot, my_lidar):
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
    
    # Lidar
    lidar = robot.getDevice('lidar')
    lidar.enable(timestep)
    lidar.enablePointCloud()
    
    
    
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        # Read the sensors:
        # Enter here functions to read sensor data, like:
        #  val = ds.getValue()
        lidarPoints = lidar.getPointCloud(); # Get the point cloud

    # Print out the x, y, z, and layer information for the first point in the point cloud    
        print("x: " + str(lidarPoints[0].x) + " y: " + str(lidarPoints[0].y) + " z: " + str(lidarPoints[0].z) + " layer: " + str(lidarPoints[0].layer_id))
        range_image = lidar.getRangeImage()
        #print(my_lidar.x)
        #point_tuple = (my_lidar.x, my_lidar.y, my_lidar.z, my_lidar.layer_id, my_lidar.time)
        #print(point_tuple)
        print("{}".format(range_image[0]))
    
        # Process sensor data here.
    
        # Enter here functions to send actuator commands, like:
        #  motor.setPosition(10.0)
        left_motor.setVelocity(max_speed*0.25)
        right_motor.setVelocity(max_speed*0.25)

# Enter here exit cleanup code.


if __name__ == "__main__":
# create the Robot instance.
    my_robot = Robot()
    my_lidar = LidarPoint()
    run_robot(my_robot, my_lidar)