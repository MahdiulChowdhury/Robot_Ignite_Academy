#! /usr/bin/env python

import rospy 
from std_srvs.srv import Empty, EmptyResponse
from move_bb8 import MoveBB8

def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_square has been called")
    movebb8_object = MoveBB8() 
    movebb8_object.move_square()
    rospy.loginfo("Finished service move_bb8_in_square that was called called")
    return EmptyResponse() 
    
    
rospy.init_node('service_move_bb8_in_square_server')
my_service = rospy.Service('/move_bb8_in_square', Empty, my_callback)
rospy.loginfo("Service /move_bb8_in_square Ready")
rospy.spin() 