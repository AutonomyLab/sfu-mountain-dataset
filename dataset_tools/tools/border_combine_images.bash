#! /bin/bash

for i in `seq -f "%05g" 1 239`
do
    str=""
    for bag in wet dry3 dusk night3
    do
        for cam in 3 4 2 0 1 5
        do
            str="$str a_raw/a_camera${cam}_place${i}_trail_${bag}_a.jpg"
        done
    done
    echo -n " $i"
    montage -resize 640x480\! -geometry +$1+$1 -tile 6x4 $str a_$2/place${i}_a.jpg
done

for i in `seq -f "%05g" 1 146`
do
    str=""
    for bag in wet dry3 dusk night3
    do
        for cam in 3 4 2 0 1 5
        do
            str="$str b_raw/b_camera${cam}_place${i}_trail_${bag}_b.jpg"
        done
    done
    echo -n " $i"
    montage -resize 640x480\! -geometry +$1+$1 -tile 6x4 $str b_$2/place${i}_b.jpg
done

