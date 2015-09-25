#! /usr/bin/env python

import fileinput
import tf

def run():
    px = 0
    py = 0
    pz = 0
    ox = 0
    oy = 0
    oz = 0
    ow = 0
    secs = 0
    nsecs = 0

    mode = "position"
    new = False

    for line in fileinput.input():
        if "nsecs" in line:
            nsecs = line.split(": ")[1].rstrip().lstrip()
        elif "secs" in line:
            secs = line.split(": ")[1].rstrip().lstrip()
            new = True
        elif "x:" in line and new:
            if mode == "position":
                px = line.split(": ")[1].rstrip().lstrip()
            else:
                ox = line.split(": ")[1].rstrip().lstrip()
        elif "y:" in line and new:
            if mode == "position":
                py = line.split(": ")[1].rstrip().lstrip()
            else:
                oy = line.split(": ")[1].rstrip().lstrip()
        elif "z:" in line and new:
            if mode == "position":
                pz = line.split(": ")[1].rstrip().lstrip()
            else:
                oz = line.split(": ")[1].rstrip().lstrip()
        elif "w:" in line and new:
            ow = line.split(": ")[1].rstrip().lstrip()
        elif "position" in line:
            mode = "position"
        elif "orientation" in line:
            mode = "orientation"
        elif "covariance" in line:
            new = False
            q = (ox, oy, oz, ow)
            e = tf.transformations.euler_from_quaternion(q)
            print "%s%s %s %s %s %s %s %s" % (secs, nsecs, px, py, pz, e[0], e[1], e[2])

if __name__ == "__main__":
    run()
