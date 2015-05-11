#! /usr/bin/env python

import fileinput
import tf
#import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

secs = 0
nsecs = 0
t = 0

first_t = -1

stamps = []

for line in fileinput.input():
    if "nsecs" in line:
        nsecs = int(line.split(": ")[1].rstrip().lstrip())

    elif "secs" in line:
        secs = int(line.split(": ")[1].rstrip().lstrip())

    elif "---" in line:
        t = "%s.%s" % (secs, nsecs)
        t = float(t)
        if first_t == -1:
            first_t = t

        t -= first_t
        stamps.append(t)

plt.scatter(range(0,len(stamps)), stamps)
plt.show()
