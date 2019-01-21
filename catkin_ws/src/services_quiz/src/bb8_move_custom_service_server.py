#! /usr/bin/env python

import rospy 
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from move_bb8 import MoveBB8

def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_square has been called")
    movebb8_object = MoveBB8() 
    repetions_of_square = request.repetitions + 1 
    new_side = request.side 
    
    for i in range (repetions_of_square): 
        rospy.loginfo("Start Movement with side ="+str(new_side) + " Repetition = "+str(i))
        movebb8_object.move_square(side = new_side)
        
    rospy.loginfo("Finished service move_bb8_in_square that was called called")
    response = BB8CustomServiceMessageResponse()
    response.success = True 
    return response
    
    
rospy.init_node('service_move_bb8_in_square_server')
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage, my_callback)
rospy.loginfo("Service /move_bb8_in_square_custom Ready")
rospy.spin() 