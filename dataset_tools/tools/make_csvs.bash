#! /bin/bash

bag=$1
cd /local_home/share/trail-mapping
mkdir -p $bag
cd $bag
mkdir -p a
cd a
extract_dat -i /local_home/share/trail-mapping/bags/outdoor/fixed/trail_$bag\_a.bag
cd ..
mkdir -p b
cd b
extract_dat -i /local_home/share/trail-mapping/bags/outdoor/fixed/trail_$bag\_b.bag
