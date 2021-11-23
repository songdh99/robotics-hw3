#!/usr/bin/env python
import rospy
import math
from common_msg.msg import position
from common_msg.srv import hypotenuse, hypotenuseResponse

def service_callback(request):
    if request.height == 0:
        calculated_hypotenuse = 0
    else:
        calculated_hypotenuse = math.sqrt((request.base*request.base) +  (request.height*request.height))
    response = hypotenuseResponse(hypotenuse=calculated_hypotenuse)
    print "===================Response =========================="
    print "Request height: ", request.height
    print "Request base: ", request.base
    print "Response hypotenuse: ", response.hypotenuse
    print "======================================================"
    return response

def callback(msg):
    print "subscribed position x: ", msg.point.x
    print "subscribed position y: ", msg.point.y
    print "subscribed position z: ", msg.point.z
    print "subscribed position time: ", msg.timestamp.data.secs%60
    print "Sub finish"

rospy.init_node('pose_subscriber')
sub = rospy.Subscriber('common_msg', position, callback)
service = rospy.Service('calculate_hypotenuse', hypotenuse, service_callback)
rospy.spin()
