#!/usr/bin/env python
import rospy
import math
from common_msg.msg import position
from common_msg.srv import hypotenuse, hypotenuseRequest

rospy.init_node('pose_publisher')
pub = rospy.Publisher('common_msg', position, queue_size=1)
requester = rospy.ServiceProxy('calculate_hypotenuse', hypotenuse)
msg = position()
count = 0
num = 0
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    if count > 100:
        count = 0    
    msg.point.x = count * 10
    msg.point.y = count + 15
    msg.point.z = count / 2
    msg.timestamp.data = rospy.get_rostime()
    second = msg.timestamp.data.secs % 60 
    pub.publish(msg)
    print "published data of x: ", msg.point.x
    print "published data of y: ", msg.point.y
    print "published data of z: ", msg.point.z
    print "published timestemp: ", second
    print "Pub finish"

    if count % 3 == 0:
        request = hypotenuseRequest(height=count, base=num)
        response = requester(request)
        print "======================Request===================="
        print "height : ", request.height
        print "base : ", request.base
        print "hypotenuse : ", response.hypotenuse
        print "================================================="
    

    count += 1
    num+=3
    rate.sleep()
