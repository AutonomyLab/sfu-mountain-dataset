#! /usr/bin/env python

import fileinput

def run():
    data = 0
    i = 0

    for line in fileinput.input():
        if "data" in line:
            data = line.split(": ")[1].rstrip().lstrip()
            print "%s %s" % (i, data)
            i += 1

if __name__ == "__main__":
    run()
