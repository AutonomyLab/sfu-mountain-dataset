#! /usr/bin/env python

import fileinput
import struct

def run():
    print "VERSION 0.7"
    print "FIELDS X Y Z rgb"
    print "SIZE 4 4 4 4"
    print "TYPE F F F F"
    print "COUNT 1 1 1 1"
    print "WIDTH FILL_ME_IN"
    print "HEIGHT 1"
    print "VIEWPOINT 0 0 0 1 0 0 0"
    print "POINTS FILL_ME_IN"
    print "DATA ascii"

    header = False
    for line in fileinput.input():
        if not header:
            header = True
        else:
            data = line.split(",")
            r = int(data[3].strip())
            g = int(data[4].strip())
            b = int(data[5].strip())
            #packed_rgb = r << 16 | g << 8 | b
            packed_rgb = struct.pack("BBBB", 0, r, g, b)
            float_rgb = struct.unpack("f", packed_rgb)[0]
            print "%s %s %s %s" % (data[0].strip(), data[1].strip(), data[2].strip(), float_rgb)

if __name__ == "__main__":
    run()
