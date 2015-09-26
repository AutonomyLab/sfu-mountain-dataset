#! /usr/bin/env python

#from __future__ import print_function
import rospy
import tf
import numpy as np
from sensor_msgs.msg import *
from geometry_msgs.msg import *
from nav_msgs.msg import *
import math
import random
import sys
import cv2
from cv_bridge import CvBridge
from threading import Lock

img_encoding = "bgr8"

#------------------------------------------------------

print_lock = Lock()
def safe_print(s):
    with print_lock:
        sys.stdout.write(s + '\n')

#------------------------------------------------------

def color_pointcloud(img, pc, camera_msg, camera_idx):
    rot = np.array([0.0, 0.0, 0.0])
    trans = np.array([0.0, 0.0, 0.0])
    fixed_frame = camera_msg.header.frame_id
    try:
        pc_fixed = tl.transformPointCloud(fixed_frame, pc)
        pc_odom = tl.transformPointCloud("odom", pc)
        points = np.array([[-p.y, -p.z, p.x] for p in pc_fixed.points])
        points_pix, jacobian = cv2.projectPoints(points, rot, trans, camera_matrix[camera_idx], camera_distortion[camera_idx])
        for i,p in enumerate(points_pix.astype(np.int32)):
            # if the point is in front of the camera and in the plane
            if (points[i,2] > 0 and p[0,0] > 0 and p[0,1] > 0 and
                    p[0,0] < img.shape[1] and p[0,1] < img.shape[0]):
                pt = (p[0,0], p[0,1])
                # X Y Z R G B
                safe_print("%s,%s,%s,%s,%s,%s" % (pc_odom.points[i].x,
                        pc_odom.points[i].y,
                        pc_odom.points[i].z,
                        img[pt[1],pt[0],2],
                        img[pt[1],pt[0],1],
                        img[pt[1],pt[0],0]))
    except tf.Exception as e:
        #print "TF Exception: %s" % e
        pass

#------------------------------------------------------

def draw_lasers(img, camera_msg, camera_idx):
    for i,pc in enumerate(scans):
        if pc != None:
            color_pointcloud(img, pc, camera_msg, camera_idx)

#------------------------------------------------------

def handle_camera(camera_msg, camera_idx):
    img = cvb.imgmsg_to_cv2(camera_msg, img_encoding)
    draw_lasers(img, camera_msg, camera_idx)

#------------------------------------------------------------

scans = []
def handle_scan(scan_msg, laser_idx):
    ranges = scan_msg.ranges
    intensities = scan_msg.intensities

    pc = PointCloud()
    pc.header = scan_msg.header
    pc.points = []

    for i,v in enumerate(ranges):
        if v >= scan_msg.range_max or v <= scan_msg.range_min or np.isnan(v) or np.isinf(v):
            continue

        else:
            theta = scan_msg.angle_min + i*scan_msg.angle_increment
            p = Point32()
            p.x = v * math.cos(theta)
            p.y = v * math.sin(theta)
            p.z = 0
            pc.points.append(p)

    scans[laser_idx] = pc

# ------- SETUP -----------------

rospy.init_node("derp", anonymous=True)
tl = tf.TransformListener()

cvb = CvBridge()
camera_matrix = []
camera_distortion = []

camera_topics = []
idx = 0
while True:
    topic = rospy.get_param("~camera%d" % idx, False)
    if topic != False:
        camera_topics.append(topic)
        mat = rospy.get_param("~camera%d_matrix" % idx, -1)
        dist = rospy.get_param("~camera%d_distortion" % idx, -1)
        camera_matrix.append(np.reshape(np.array(mat), (3,3)))
        camera_distortion.append(np.array(dist))
        idx += 1
    else:
        break
camera_counts = [0] * idx

laser_topics = []
idx = 0
while True:
    topic = rospy.get_param("~laser%d" % idx, False)
    if topic != False:
        laser_topics.append(topic)
        idx += 1
    else:
        break
scans = [None] * idx
scan_counts = [0] * idx

for i,v in enumerate(laser_topics):
    rospy.Subscriber(v, LaserScan, handle_scan, callback_args=i)
for i,v in enumerate(camera_topics):
    rospy.Subscriber(v, Image, handle_camera, callback_args=i)

while not rospy.is_shutdown():
    print "x,y,z,r,g,b"
    rospy.spin()
