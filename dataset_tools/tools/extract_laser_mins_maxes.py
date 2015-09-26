#! /usr/bin/env python

import fileinput

def run():
    mins = None
    maxes = None
    count = 0

    for line in fileinput.input():
        if "ranges" in line:
            ranges = [float(a) for a in line.split(": ")[1].rstrip().lstrip().replace("[","").replace("]","").split(", ")]

            if mins == None:
                mins = [1e8] * len(ranges)
                maxes = [0] * len(ranges)

            for i,r in enumerate(ranges):
                if r > maxes[i]: maxes[i] = r
                if r < mins[i]: mins[i] = r

            with open("laser_mins.dat", "w") as f:
                for r in mins:
                    f.write("%s\n" % r)
            with open("laser_maxes.dat", "w") as f:
                for r in maxes:
                    f.write("%s\n" % r)

            print "read msg %s" % count

            count += 1

if __name__ == "__main__":
    run()
