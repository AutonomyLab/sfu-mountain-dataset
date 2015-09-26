#! /usr/bin/env python

from __future__ import print_function
import rospy
import tf
from sensor_msgs.msg import *
from geometry_msgs.msg import *
import math
import random
import sys

tf_buffer = []

def handle_scan(scan_msg):
    global tf_buffer 

    ranges = scan_msg.ranges
    intensities = scan_msg.intensities

    pc = PointCloud()
    pc.header = scan_msg.header
    pc.points = []
    intensity_channel = ChannelFloat32()
    intensity_channel.name = "intensity"
    intensity_channel.values = []
    pc.channels = [intensity_channel]

    for i,v in enumerate(ranges):
        if v >= scan_msg.range_max or v <= scan_msg.range_min or math.isnan(v):
            continue

        theta = scan_msg.angle_min + i*scan_msg.angle_increment

        p = Point32()
        p.x = v * math.cos(theta)
        p.y = v * math.sin(theta)
        p.z = 0

        pc.points.append(p)

        if len(intensities) > i:
            pc.channels[0].values.append(intensities[i])
        else:
            pc.channels[0].values.append(1000)

    tf_buffer.append(pc)
    new_tf_buffer = []

    for elem in tf_buffer:
        try:
            pc_fixed = tl.transformPointCloud(fixed_frame, elem)

            for i,v in enumerate(pc_fixed.points):
                print("%s %s %s %s" % (scan_msg.header.stamp, v.x, v.y, v.z))

        except:
            new_tf_buffer.append(elem)

    tf_buffer = new_tf_buffer


rospy.init_node("derp", anonymous=True)

tl = tf.TransformListener()
fixed_frame = rospy.get_param("~fixed_frame", "base_link")

rospy.Subscriber("/lidar/scan", LaserScan, handle_scan)

while not rospy.is_shutdown():
    rospy.spin()
