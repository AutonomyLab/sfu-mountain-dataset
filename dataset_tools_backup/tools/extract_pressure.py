#! /usr/bin/env python

import fileinput

def run():
    data = 0
    nsecs = 0
    secs = 0

    for line in fileinput.input():
        if "nsecs" in line:
            nsecs = line.split(": ")[1].rstrip().lstrip()
        elif "secs" in line:
            secs = line.split(": ")[1].rstrip().lstrip()
        elif "fluid_pressure" in line:
            data = line.split(": ")[1].rstrip().lstrip()
            print "%s.%s %s" % (secs, nsecs, data)

if __name__ == "__main__":
    run()
