#! /usr/bin/env python

import fileinput
import tf


last_seq = -1
for line in fileinput.input():
    if "seq" in line:
        seq = int(line.split(": ")[1].rstrip().lstrip())
        if last_seq == -1:
            last_seq = seq - 1
        if seq != last_seq + 1:
            print "Expected seq %d, got seq %d" % (last_seq+1, seq)
        last_seq = seq
