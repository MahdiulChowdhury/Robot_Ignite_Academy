import rospkg 
import rospy 
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest

rospy.init_node('service_execute_trajectory_client')
rospy.wait_for_service('/execute_trajectory')
execute_trajectory_service_client = rospy.ServiceProxy('/execute_trajectory', ExecTraj)
execute_trajectory_request_object = ExecTrajRequest()


rospack = rospkg.RosPack() 
trajectory_file_path = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"
execute_trajectory_request_object.file = trajectory_file_path
result = execute_trajectory_service_client(execute_trajectory_request_object)
print result # Print the result type ExecTrajResponse


