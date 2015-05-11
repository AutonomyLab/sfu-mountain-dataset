#! /usr/bin/env python

import fileinput

def run():
    nsecs = 0
    secs = 0
    x = 0
    y = 0
    z = 0

    for line in fileinput.input():
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
        elif "orientation" in line:
            print "%s.%s %s" % (secs,nsecs, z)

if __name__ == "__main__":
    run()
