#! /usr/bin/env python

import fileinput
import tf
import sys
import math
import matplotlib.pyplot as plt

def run():
    x = 0
    y = 0
    z = 0
    w = 0
    nsecs = 0
    secs = 0

    data = []

    fig=plt.figure()

    plt.ion()
    plt.show()

    i = 0

    for line in sys.stdin:
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
            """
            print "%s.%s %s" % (secs,nsecs, e[0])
            print "%s.%s %s" % (secs,nsecs, e[1])
            print "%s.%s %s" % (secs,nsecs, e[2])
            """
            x = math.degrees(e[0])
            y = math.degrees(e[1])
            z = math.degrees(e[2])

            data.append(z)

            i += 1
            if (i % 100 == 0):
                plt.plot(data)
                plt.draw()

            print "%s %s %s" % (x,y,z)

if __name__ == "__main__":
    run()
