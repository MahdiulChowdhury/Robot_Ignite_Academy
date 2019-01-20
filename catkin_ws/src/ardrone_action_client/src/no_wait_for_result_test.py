#! /usr/bin/env python 

import rospy 
import time 
import actionlib 
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult,ArdroneFeedback


PENDING = 0 
ACTIVE = 1 
DONE = 2 
WARN = 3 
ERROR = 4 

nImage = 1 

def feedback_callback (feedback):
    
    global nImage
    print('[Feedback] image n.%d received'%nImage)
    nImage += 1 
    
# initialzes the action client node 
rospy.init_node('example_no_waitforresult_action_client_node')

action_server_name = '/ardrone_action_server'
client = actionlib.SimpleActionClient(action_server_name, ArdroneAction)


rospy.loginfo('Waiting for action server'+action_server_name)
client.wait_for_server() 
rospy.loginfo('Action Server Found ...'+action_server_name)

goal = ArdroneGoal() 
goal.nseconds = 10 

client.send_goal(goal,feedback_cb = feedback_callback)

state_result = client.get_state() 
rate = rospy.Rate(1)

rospy.loginfor("state_result:"+str(state_result))

while state_result < DONE: 
    rospy.loginfo ("Doing Stuff while waiting for the server to give a result ...")
    rate.sleep()
    state_result = client.get_state() 
    rospy.loginfo ("state_result:"+str(state_result))

rospy.loginfo ("[Result] State :"+str(state_result))
if state_result == ERROR: 
    rospy.logerr("Something went wrong in the Server Side ")
if state_result == WARN: 
    rospy.lowarn("There is a warning in the Server Side")
    