#! /usr/bin/env python

import fileinput

def run():
    x = 0
    y = 0

    for line in fileinput.input():
        if "x" in line:
            x = line.split(": ")[1].rstrip().lstrip()
        elif "y" in line:
            y = line.split(": ")[1].rstrip().lstrip()
        elif "angular" in line:
            print "%s %s" % (x, y)

if __name__ == "__main__":
    run()
