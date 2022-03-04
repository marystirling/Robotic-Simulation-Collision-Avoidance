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
    
    # Lidar
    lidar = robot.getDevice('lidar')
    lidar.enable(timestep)
    lidar.enablePointCloud()
    
    # horizontalResolution is how many distance points are calculated in one layer
    horizontalResolution = lidar.getHorizontalResolution();
    print(f"horizontal resolution: {horizontalResolution}")
    
    # numberOfLayers is how many layers distance readings will be done on
    numberOfLayers = lidar.getNumberOfLayers();
 
    print(f"number of layers: {numberOfLayers}")
    
    # fov is the field of view of LiDAR distance readings
    fov = lidar.getFov()
    print(f"field of view: {fov}")
    
    # degrees is the exact degrees from the robot with fov range
    degrees = fov * 180 / math.pi
    print(f"degrees in field of view: {degrees}")
    
    # creates an empty list of distance measurements
    distance_list = []
    
    # calculates the angle between each laser within the fov
    split_degrees = degrees / horizontalResolution
    print(f"the angle between each laser is: {split_degrees}")
    
    counter = 0
    
  
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        

        
       
        # Read the sensors:
        # Enter here functions to read sensor data, like:
        #  val = ds.getValue()
        lidarPoints = lidar.getPointCloud(); # Get the point cloud

    # Print out the x, y, z, and layer information for the first point in the point cloud    
        #print("x: " + str(lidarPoints[0].x) + " y: " + str(lidarPoints[0].y) + " z: " + str(lidarPoints[0].z) + " layer: " + str(lidarPoints[0].layer_id))
        range_image = lidar.getRangeImage()
        #print(range_image)

            #print(f"the get range position 1 is {range_image[0]}")
        
        # laser_counter keeps track of what distance angle measurement in each layer
        laser_counter = counter % horizontalResolution + 1
        print(laser_counter)
        
        # point_degree is the degree of each laser distance measurmeent within each layer
        point_degree = split_degrees * laser_counter
        print(point_degree)
        
        print(f"the distance from an object is: {range_image[laser_counter -1]}")
        
   #     if range_image[0] != float('inf'):
        
        # point_tuple keeps track of the degree of each distance measurement and the distance of that point
        point_tuple  = (point_degree, range_image[0])
        distance_list.append(point_tuple)
        print(point_tuple)
       
        #if range_image[0] != float('inf'):
            #if range_image[0] < 2:
                #print(f"distance is {range_image[0]} meters")
                #print(fov)
    
        # Process sensor data here.
    
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