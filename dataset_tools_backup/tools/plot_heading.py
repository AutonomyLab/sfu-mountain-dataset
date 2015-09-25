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

    d = 0

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
        elif "data:" in line:
            d = line.split(": ")[1].rstrip().lstrip()
        elif "---" in line:
            data.append(d)
            i += 1
            if (i % 10 == 0):
                plt.plot(data)
                plt.draw()
            else:
                print len(data)

if __name__ == "__main__":
    run()
