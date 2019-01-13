#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32 
from geometry_msgs.msg import Twist

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
var = Twist()


while not rospy.is_shutdown(): 
  pub.publish(var)
  var.linear.x = .5
  var.angular.z = .2
  rate.sleep()