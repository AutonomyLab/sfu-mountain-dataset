#! /usr/bin/env python

import fileinput, os, random

def run():
    subsample = float(os.getenv("SUBSAMPLE", "1.0"))

    for line in fileinput.input():
        if random.random() <= subsample:
            print line.rstrip()

if __name__ == "__main__":
    run()
