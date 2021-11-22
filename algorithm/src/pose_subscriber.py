#!/usr/bin/env python
import rospy
from common_msg.msg import position

def callback(msg):
    print "subscribed position x: ", msg.point.x
    print "subscribed position y: ", msg.point.y
    print "subscribed position z: ", msg.point.z
    print "subscribed position time: ", msg.timestamp.data.secs%60
    print "Sub finish"

rospy.init_node('pose_subscriber')
sub = rospy.Subscriber('common_msg', position, callback)
rospy.spin()
