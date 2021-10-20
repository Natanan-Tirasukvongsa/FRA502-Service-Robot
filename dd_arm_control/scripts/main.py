import rospy 
from std_msgs.msg import Float64

def talker():
    pub = rospy.Publisher('/dd/joint1_position_controller/command',Float64,queue_size=10)
    rospy.init_node('dd_talker',anonymous=True)
    rate = rospy.Rate(10) #10 hz
    while not rospy.is_shutdown():
        position = 0.0
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()
if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInitException:
        pass