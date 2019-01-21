#! /usr/bin/env python

import rospkg 
import rospy 

from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest

rospy.init_node('service_move_bb8_in_square_custom_client') #initialize ROS node with the name service_move_bb8_in_square_custom_client 
rospy.wait_for_service('/move_bb8_in_square_custom') #wait for the service client /move_bb8_in_sqaure to be running 
move_bb8_in_square_service_client = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage) ##create the connection to the service
move_bb8_in_square_request_object = BB8CustomServiceMessageRequest() #create an instance of the request class 

move_bb8_in_square_request_object.side = 0.2 
move_bb8_in_square_request_object.repetitions = 2 

rospy.loginfo(" Small Squares...")
result = move_bb8_in_square_service_client(move_bb8_in_square_request_object) #send the trajectory/command to the server to be used py .py
rospy.loginfo(str(result)) #Print the result 

move_bb8_in_square_request_object.side = 0.6 
move_bb8_in_square_request_object.repetitions = 2 

rospy.loginfo("Start Two big Squares...")
result = move_bb8_in_square_service_client(move_bb8_in_square_request_object) #send the trajectory/command to the server to be used py .py
rospy.loginfo(str(result)) #Print the result 

rospy.loginfo("END of Service call...")
