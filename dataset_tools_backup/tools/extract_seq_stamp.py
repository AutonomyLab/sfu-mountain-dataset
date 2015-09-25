#! /usr/bin/env python

import fileinput

def run():
    first_secs = 0
    seq = 0
    secs = 0
    nsecs = 0

    for line in fileinput.input():
        if "seq" in line:
            seq = int(line.split(": ")[1].rstrip().lstrip())
        elif "nsecs" in line:
            nsecs = int(line.split(": ")[1].rstrip().lstrip())
        elif "secs" in line:
            secs = int(line.split(": ")[1].rstrip().lstrip())
            if first_secs == 0:
                first_secs = secs
            secs -= first_secs
        elif "frame_id" in line:
            print "%s %s.%s" % (seq, secs, nsecs)

if __name__ == "__main__":
    run()
