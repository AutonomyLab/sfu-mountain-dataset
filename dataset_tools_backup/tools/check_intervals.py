#! /usr/bin/env python

import fileinput
import tf
#import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

secs = 0
nsecs = 0
t = 0

last_t = -1

intervals = []

for line in fileinput.input():
    if "nsecs" in line:
        nsecs = int(line.split(": ")[1].rstrip().lstrip())

    elif "secs" in line:
        secs = int(line.split(": ")[1].rstrip().lstrip())

    elif "---" in line:
        t = "%s.%s" % (secs, nsecs)
        t = float(t)
        if last_t == -1:
            last_t = t
        else:
            interval = t - last_t
            last_t = t
            intervals.append(interval)

absint = [abs(i) for i in intervals]

print "min interval: %s s at position %s/%s" % (min(intervals), intervals.index(min(intervals)), len(intervals))
print "min abs interval: %s s at position %s/%s" % (min(absint), intervals.index(min(absint)), len(intervals))
print "max interval: %s s at position %s/%s" % (max(intervals), intervals.index(max(intervals)), len(intervals))
print "mean interval: %s s" % np.mean(np.array(intervals))
print "standard deviation: %s s" % np.std(np.array(intervals))

plt.hist(intervals, 80)
plt.show()
