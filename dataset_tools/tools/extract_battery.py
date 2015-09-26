#! /usr/bin/env python

import fileinput

def run():
    charge = 0
    nsecs = 0
    secs = 0

    for line in fileinput.input():
        if "nsecs" in line:
            nsecs = line.split(": ")[1].rstrip().lstrip()
        if "secs" in line:
            secs = line.split(": ")[1].rstrip().lstrip()
        if "charge" in line:
            charge = line.split(": ")[1].rstrip().lstrip()
            print "%s.%s %s" % (secs, nsecs, charge)

if __name__ == "__main__":
    run()
