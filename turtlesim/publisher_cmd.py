import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def trans_cmdVel(data):
  rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
  if data.data == "up":
    rospy.loginfo(data.linear.2, data.linear.0)
  else if data.data == "down":
    rospy.loginfo(data.linear.-2,data.linear.0)
  else if data.data == "left":
    rospy.loginfo(data.linear.0, data.linear.2)
  else if data.data == "right":
    rospy.loginfo(data.linear.0, data.linear.-2)

def listener():

  rospy.init_node('listener', anonymous=True)

  rospy.Subscriber("/move_command", String, trans_cmdVel)

  # spin() simply keeps python from exiting until this node is stopped
  rospy.spin()

if __name__ == '__main__':
  listener()
