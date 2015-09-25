#! /usr/bin/env python

import fileinput
import math

def run():
    x = 0
    y = 0
    nsecs = 0
    secs = 0

    for line in fileinput.input():
        if "nsecs" in line:
            nsecs = line.split(": ")[1].rstrip().lstrip()
        elif "secs" in line:
            secs = line.split(": ")[1].rstrip().lstrip()
        elif "x" in line:
            x = float(line.split(": ")[1].rstrip().lstrip())
        elif "y" in line:
            y = float(line.split(": ")[1].rstrip().lstrip())
        elif "angular" in line:
            heading = math.degrees(math.atan2(y,x))
            print "%s.%s %s" % (secs,nsecs,heading)

if __name__ == "__main__":
    run()
