#!/usr/bin/env python
import rospy
from common_msg.msg import position

rospy.init_node('pose_publisher')
pub = rospy.Publisher('common_msg', position, queue_size=1)
msg = position()
count = 0
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    if count > 100:
        count = 0    
    msg.point.x = count * 10
    msg.point.y = count + 10
    msg.point.z = count / 2
    msg.timestamp.data = rospy.get_rostime()
    second = msg.timestamp.data.secs % 60 
    pub.publish(msg)
    print "published data of x: ", msg.point.x
    print "published data of y: ", msg.point.y
    print "published data of z: ", msg.point.z
    print "published timestemp: ", second
    print "Pub finish"

    count += 1
    rate.sleep()
