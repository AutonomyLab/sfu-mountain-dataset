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

laser_colors = [(255, 255, 0),
        (0, 255, 255),
        (255, 0, 255)]

odom_colors = [(255, 0, 0),
        (0, 255, 0),
        (0, 0, 255)]

odom_buffer_size = 200
odom_subsample = 5
scan_subsample = 1
camera_subsample = 1
point_size = 2
legend_x = 10
legend_y_spacing = 20
legend_size = 0.5
legend_thickness = 2
img_encoding = "bgr8"

#------------------------------------------------------

def draw_pointcloud(img, pc, camera_msg, camera_idx, color):
    rot = np.array([0.0, 0.0, 0.0])
    trans = np.array([0.0, 0.0, 0.0])
    fixed_frame = camera_msg.header.frame_id
    try:
        pc_fixed = tl.transformPointCloud(fixed_frame, pc)
        points = np.array([[-p.y, -p.z, p.x] for p in pc_fixed.points])
        points_front = points[points[:,2] > 0]
        if points_front.shape[0] > 0:
            points_pix, jacobian = cv2.projectPoints(points_front, rot, trans, camera_matrix[camera_idx], camera_distortion[camera_idx])
            for i,p in enumerate(points_pix.astype(np.int32)):
                pt = (p[0,0], p[0,1])
                distance_coefficient = 1.0 / max(1,math.log(points_front[i,2], 1.5))
                c = (int(color[0]*distance_coefficient), int(color[1]*distance_coefficient), int(color[2]*distance_coefficient))
                cv2.circle(img, pt, point_size, c, -1)
    except tf.Exception as e:
        #print "TF Exception: %s" % e
        pass

#------------------------------------------------------

def draw_legend(img, text, idx, color):
    cv2.putText(img, text, (legend_x, (idx+1)*legend_y_spacing), cv2.FONT_HERSHEY_SIMPLEX, legend_size, color, legend_thickness)

#------------------------------------------------------

def draw_lasers(img, camera_msg, camera_idx):
    for i,pc in enumerate(scans):
        if pc != None:
            draw_pointcloud(img, pc, camera_msg, camera_idx, laser_colors[i%len(laser_colors)])
            draw_legend(img, laser_topics[i], i, laser_colors[i%len(laser_colors)])

#------------------------------------------------------

def draw_odoms(img, camera_msg, camera_idx):
    for i,odom_points in enumerate(odoms):
        pc = PointCloud()
        pc.points = []
        for o in odom_points:
            pc.header = o.header
            p = Point32()
            p.x = o.pose.pose.position.x
            p.y = o.pose.pose.position.y
            p.z = o.pose.pose.position.z
            pc.points.append(p)

        if len(pc.points) > 0:
            draw_pointcloud(img, pc, camera_msg, camera_idx, odom_colors[i%len(odom_colors)]) 
            draw_legend(img, odom_topics[i], (i+len(scans)), odom_colors[i%len(odom_colors)])

#------------------------------------------------------

def handle_camera(camera_msg, camera_idx):
    if camera_counts[camera_idx] == 0:
        img = cvb.imgmsg_to_cv2(camera_msg, img_encoding)
        draw_lasers(img, camera_msg, camera_idx)
        draw_odoms(img, camera_msg, camera_idx)
        camera_publishers[camera_idx].publish(cvb.cv2_to_imgmsg(img, img_encoding))
    camera_counts[camera_idx] = (camera_counts[camera_idx]+1) % camera_subsample

#------------------------------------------------------------

odoms = []
odom_counts = []
def handle_odom(odom_msg, odom_idx):
    if odom_counts[odom_idx] == 0:
        odoms[odom_idx].append(odom_msg)
        odoms[odom_idx] = odoms[odom_idx][-min(odom_buffer_size, len(odoms[odom_idx])):]
    odom_counts[odom_idx] = (odom_counts[odom_idx]+1) % odom_subsample

#------------------------------------------------------------

scans = []
def handle_scan(scan_msg, laser_idx):
    if scan_counts[laser_idx] == 0:
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
    
    scan_counts[laser_idx] = (scan_counts[laser_idx]+1) % scan_subsample

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

        rospy.loginfo("camera%d: %s" % (idx, camera_topics[-1]))
        rospy.loginfo("camera matrix: %s" % camera_matrix[-1])
        rospy.loginfo("distortion: %s" % camera_distortion[-1])

        idx += 1
    else:
        break
camera_counts = [0] * idx

camera_publishers = [rospy.Publisher("%s_viz" % t, Image, queue_size = 3) for t in camera_topics]

laser_topics = []
idx = 0
while True:
    topic = rospy.get_param("~laser%d" % idx, False)
    if topic != False:
        laser_topics.append(topic)
        rospy.loginfo("laser%d: %s" % (idx, laser_topics[-1]))
        idx += 1
    else:
        break
scans = [None] * idx
scan_counts = [0] * idx

odom_topics = []
idx = 0
while True:
    topic = rospy.get_param("~odom%d" % idx, False)
    if topic != False:
        odom_topics.append(topic)
        rospy.loginfo("odom%d: %s" % (idx, odom_topics[-1]))
        idx += 1
    else:
        break
odoms = [[]] * idx
odom_counts = [0] * idx

for i,v in enumerate(laser_topics):
    rospy.Subscriber(v, LaserScan, handle_scan, callback_args=i)
for i,v in enumerate(camera_topics):
    rospy.Subscriber(v, Image, handle_camera, callback_args=i)
for i,v in enumerate(odom_topics):
    rospy.Subscriber(v, Odometry, handle_odom, callback_args=i)

while not rospy.is_shutdown():
    rospy.spin()
