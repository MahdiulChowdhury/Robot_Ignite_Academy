#! /usr/bin/env python

import rospy

from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan


def collision_avoidance(msg):
    length = len(msg.ranges) ##720
    
    print msg.ranges[360] #We print the distance to an obstacle in front of the robot

#If the distance to an obstacle in front of the robot is bigger than 1 meter, the robot will move forward
    if msg.ranges[360] > 1:
        move.linear.x = 0.1
        move.angular.z = 0.0

#If the distance to an obstacle in front of the robot is smaller than 1 meter, the robot will turn left
    if msg.ranges[360] < 1: 
        move.linear.x = 0.0
        move.angular.z = 0.2
        
#If the distance to an obstacle at the left side of the robot is smaller than 0.3 meters, the robot will turn right
    if msg.ranges[719] < 0.5:
        move.linear.x = 0.0
        move.angular.z = -0.2
        
#If the distance to an obstacle at the right side of the robot is smaller than 0.3 meters, the robot will turn left
    if msg.ranges[0] < 0.5:
        move.linear.x = 0.0
        move.angular.z = 0.2
      
      
    pub.publish(move)

#initializing the node 
rospy.init_node('topics_quiz_node') 
#velocity command will be published to /cmd_vel topic 
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
#subscribing to topic /laser/scan and call collision_avoidance function as the scan data as parameter
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, collision_avoidance)   # Create a Subscriber object that will listen to the /kobuki/laser/scan
move = Twist()
rospy.spin()

