#! /usr/bin/env python 
import rospy 
import time 
import actionlib
from ardrone_as.msg import ArdroneAction,ArdroneGoal, ArdroneResult, ArdroneFeedback

def feedback_callback(feedback):
    global nImage 
    print('[Feedback image n.%d receieved'%nImage)
    nImage += 1


#initializes the action client node 
rospy.init_node('drone_action_client')

#create the connection to the action server 
client = actionlib.SimpleActionClient('/ardrone_action_server',ArdroneAction)
#waits until the action server is up and running 
client.wait_for_server()

#creates a goal to send to the action server 
goal = ArdroneGoal()
#indicates, take pictures along 10 seconds
goal.nseconds = 10 

#sends the goal to the action server with feedback as callback function 
client.send_goal (goal,feedback_cb = feedback_callback)

client.wait_for_result() 

print('[Result] State: %d'%(client.get_state()))