#! /usr/bin/env python

import fileinput, os, sys

# to know where we are
read_width = False
read_height = False
read_camera_matrix = False
read_distortion = False
read_rectification = False
read_projection = False

count = 0
buf = []

try:
    camname = sys.argv[2]
    filename = sys.argv[1]
except Exception as e:
    print "Usage: ./ost_to_yaml.py <camera_name> <ost_file_name>"
    sys.exit(1)

with open(filename, "r") as f:
    for line in f.readlines():
        if read_width:
            print "image_width: %s" % line.rstrip().lstrip()
            read_width = False
        elif read_height:
            print "image_height: %s" % line.rstrip().lstrip()
            print "camera_name: " + camname
            read_height = False
        elif read_camera_matrix:
            if count < 3:
                buf.extend(line.lstrip().rstrip().split(" "))
                count += 1
            else:
                print "camera_matrix: !!opencv-matrix"
                print "  rows: 3"
                print "  cols: 3"
                print "  dt: d"
                print "  data: %s" % [float(a) for a in buf]
                read_camera_matrix = False
        elif read_distortion:
            print "distortion_model: plumb_bob"
            print "distortion_coefficients: !!opencv-matrix"
            print "  rows: 1"
            print "  cols: 5"
            print "  dt: d"
            print "  data: %s" % [float(a) for a in line.lstrip().rstrip().split(" ")]
            read_distortion = False
        elif read_rectification:
            if count < 3:
                buf.extend(line.lstrip().rstrip().split(" "))
                count += 1
            else:
                print "rectification_matrix: !!opencv-matrix"
                print "  rows: 3"
                print "  cols: 3"
                print "  dt: d"
                print "  data: %s" % [float (a) for a in buf]
                read_rectification = False
        elif read_projection:
            if count < 3:
                buf.extend(line.lstrip().rstrip().split(" "))
                count += 1
            else:
                print "projection_matrix: !!opencv-matrix"
                print "  rows: 3"
                print "  cols: 4"
                print "  dt: d"
                print "  data: %s" % [float(a) for a in buf]
                read_projection = False

        if "width" in line:
            read_width = True
            count = 0
            buf = []
        elif "height" in line:
            read_height = True
            count = 0
            buf = []
        elif "camera matrix" in line:
            read_camera_matrix = True
            count = 0
            buf = []
        elif "distortion" in line:
            read_distortion = True
            count = 0
            buf = []
        elif "rectification" in line:
            read_rectification = True
            count = 0
            buf = []
        elif "projection" in line:
            read_projection = True
            count = 0
            buf = []
