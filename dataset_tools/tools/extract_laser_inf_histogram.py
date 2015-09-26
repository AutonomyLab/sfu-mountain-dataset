#! /usr/bin/env python

import fileinput

def run():
    bins = None
    count = 0

    for line in fileinput.input():
        if "ranges" in line:
            ranges_string = line.split(": ")[1].rstrip().lstrip()
            ranges = ranges_string[1:-1].split(", ")
            count += 1
            if bins == None:
                bins = [0]*(len(ranges)+1)

            for i in xrange(0,len(ranges)):
                if ranges[i] == "inf":
                    bins[i] += 1

            norm_bins = [0]*len(bins)
            for i in xrange(0,len(bins)):
                norm_bins[i] = bins[i] / float(count)

            print " ".join(map(str,norm_bins))

if __name__ == "__main__":
    run()
