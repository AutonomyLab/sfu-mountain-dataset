#! /usr/bin/env python

import fileinput
import tf

def run():
    x = 0
    y = 0
    z = 0
    w = 0
    nsecs = 0
    secs = 0

    for line in fileinput.input():
        if "nsecs" in line:
            nsecs = line.split(": ")[1].rstrip().lstrip()
        elif "secs" in line:
            secs = line.split(": ")[1].rstrip().lstrip()
        elif "x:" in line:
            x = line.split(": ")[1].rstrip().lstrip()
        elif "y:" in line:
            y = line.split(": ")[1].rstrip().lstrip()
        elif "z:" in line:
            z = line.split(": ")[1].rstrip().lstrip()
        elif "w:" in line:
            w = line.split(": ")[1].rstrip().lstrip()
        elif "orientation_covariance" in line:
            q = (x,y,z,w)
            e = tf.transformations.euler_from_quaternion(q)
            print "%s.%s %s" % (secs,nsecs, e[0])
            print "%s.%s %s" % (secs,nsecs, e[1])
            print "%s.%s %s" % (secs,nsecs, e[2])

if __name__ == "__main__":
    run()
