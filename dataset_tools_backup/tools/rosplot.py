#! /usr/bin/env python

import fileinput
import tf
import sys
import math
import matplotlib.pyplot as plt
import os

def run():
    if "--help" in sys.argv or "-h" in sys.argv:
        print """
        usage: autonomy_plot.py [ --time ] [ -f <comma-separated-field-indices> ]"""
        sys.exit(0)

    fields = [0,1]

    time_series = "--time" in sys.argv
    if time_series:
        fields = [0]

    for i,arg in enumerate(sys.argv):
        if arg == "-f":
            fields = []
            for f in sys.argv[i+1].split(","):
                fields.append(int(f)) 

    if len(fields) == 1:
        time_series = True

    x = []
    y = []

    plt.ion()
    #plt.plot(x,y)
    plt.show()

    last_line = ""

    while True:
        line = sys.stdin.readline()
        if not "field" in line and last_line != line:
            if time_series:
                #x.append(len(x))
                #y.append(float(line.split(",")[fields[0]]))
                x_val = len(x)
                y_val = float(line.split(",")[fields[0]])
            else:
                if "," in line:
                    #x.append(float(line.split(",")[fields[0]]))
                    #y.append(float(line.split(",")[fields[1]]))
                    x_val = float(line.split(",")[fields[0]])
                    y_val = float(line.split(",")[fields[1]])
                else:
                    #x.append(float(line.split(" ")[fields[0]]))
                    #y.append(float(line.split(" ")[fields[1]]))
                    x_val = float(line.split(",")[fields[0]])
                    y_val = float(line.split(",")[fields[1]])

            plt.plot(x_val,y_val,"bo")
            plt.draw()
            last_line = line

if __name__ == "__main__":
    run()
