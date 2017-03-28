import rospy
from std_msgs.msg import String

def callback(data):
        count = count + 1
        rospy.loginfo(count)

def listener():
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("/move_comand", String, callback)
        rospy.spin();

count = 0
if __name__ == '__main__':
        listener()
