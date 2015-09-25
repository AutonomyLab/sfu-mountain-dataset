#! /usr/bin/env python

import sys

HIST_BINS = 40

huge = False

dat = []

with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        dat.append(float(line))
        if dat[-1] > 10000:
            huge = True

if huge:
    dat = [a/1000.0 for a in dat]

mn = min(dat)
mx = max(dat)

if mn == mx:
    sys.exit(1)

binwidth = (mx-mn)/HIST_BINS
hist = [0] * HIST_BINS
for d in dat:
    hist[min(int((d-mn)/binwidth), 39)] += 1

for i,h in enumerate(hist):
    print "%s %s" % (i*binwidth + mn, h)
