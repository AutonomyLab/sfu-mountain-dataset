#! /usr/bin/env python

import fileinput

def run():
    for line in fileinput.input():
        print ", ".join(line.split())

if __name__ == "__main__":
    run()
