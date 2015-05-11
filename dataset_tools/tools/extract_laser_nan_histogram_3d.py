#! /usr/bin/env python

import fileinput
import numpy as np

def run():
    bins = []
    count = 0
    window = 1000

    for line in fileinput.input():
        if "ranges" in line:
            ranges = line.split(": ")[1].rstrip().lstrip()[1:-1].split(", ")
            count += 1

            b = [0]*181

            for i in xrange(0,len(ranges)):
                if ranges[i] == "nan":
                    b[i] = 1

            bins.append(b)

            if count >= window:
                m = np.array(bins[-window:])
                sums = np.sum(m, axis=0)

                for i in xrange(0, sums.shape[0]):
                    print "%s %s %s" % (count, i, sums[i]/float(window))

if __name__ == "__main__":
    run()
