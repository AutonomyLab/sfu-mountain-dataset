#! /usr/bin/env python

import fileinput

def run():
    x = 0
    y = 0
    z = 0
    secs = 0
    nsecs = 0

    for line in fileinput.input():
        if "nsecs" in line:
            nsecs = line.split(": ")[1].rstrip().lstrip()
        elif "secs" in line:
            secs = line.split(": ")[1].rstrip().lstrip()
        elif "latitude:" in line:
            x = line.split(": ")[1].rstrip().lstrip()
        elif "longitude:" in line:
            y = line.split(": ")[1].rstrip().lstrip()
        elif "altitude:" in line:
            z = line.split(": ")[1].rstrip().lstrip()
        elif "---" in line:
            print "%s %s %s" % (x, y, z)

if __name__ == "__main__":
    run()
