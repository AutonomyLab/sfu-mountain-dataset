#! /bin/bash

for bag in dry3 wet dusk night3
do
    for part in a b
    do
        cd /local_home/share/trail-mapping
        cd $bag/$part
        mkdir -p plots

        for f in csv/1d-seq-stamp-*
        do
            awk -F, 'NR == 1{cold = $2; next} {print $2 - old; old = $2}' $f > $f.diff.csv
        done
        rm csv/1d-seq-stamp-*.diff.csv.diff.csv

        for csv in csv/1d-*.csv
        do
            echo "---------------"
            echo "$bag/$part/$csv"
            gnuplot -e "set datafile separator ','; set terminal png size 800,600 enhanced font 'Helvetica,20'; set output '$csv.png'; plot '$csv' w d"
        done

        for csv in csv/2d-*.csv
        do
            echo "---------------"
            echo "$bag/$part/$csv"
            gnuplot -e "set datafile separator ','; set terminal png size 800,600 enhanced font 'Helvetica,20'; set output '$csv.png'; plot '$csv' w d"
        done

        for csv in csv/3d-*.csv
        do
            echo "---------------"
            echo "$bag/$part/$csv"
            gnuplot -e "set datafile separator ','; set terminal png size 800,600 enhanced font 'Helvetica,20'; set output '$csv.png'; splot '$csv' w d"
        done

        for topic in encoder navsat_enu
        do
            gnuplot -e "set datafile separator ','; set terminal png size 800,600 enhanced font 'Helvetica,20'; set output 'csv/1d-vxyz-$topic.png'; plot 'csv/1d-vx-$topic.csv' w d, 'csv/1d-vy-$topic.csv' w d, 'csv/1d-vz-$topic.csv' w d"
        done

        gnuplot -e "set datafile separator ','; set terminal png size 800,600 enhanced font 'Helvetica,20'; set output 'csv/1d-axyz-imu_data.png'; plot 'csv/1d-ax-imu_data.csv' w d, 'csv/1d-ay-imu_data.csv' w d, 'csv/1d-az-imu_data.csv' w d"

        for topic in encoder imu_data navsat_enu husky_cmd_vel
        do
            gnuplot -e "set datafile separator ','; set terminal png size 800,600 enhanced font 'Helvetica,20'; set output 'csv/1d-vrpy-$topic.png'; plot 'csv/1d-vroll-$topic.csv' w d, 'csv/1d-vpitch-$topic.csv' w d, 'csv/1d-vyaw-$topic.csv' w d"
        done

        for topic in encoder imu_data navsat_enu
        do
            gnuplot -e "set datafile separator ','; set terminal png size 800,600 enhanced font 'Helvetica,20'; set output 'csv/1d-rpy-$topic.png'; plot 'csv/1d-roll-$topic.csv' w d, 'csv/1d-pitch-$topic.csv' w d, 'csv/1d-yaw-$topic.csv' w d"
        done

        #echo "moving csv/*.png to plots/"
        mv csv/*.png plots/
        rename -f 's/.csv.png/.png/' plots/*.png
    done
done

mkdir -p combined_plots

for part in a b
do
    cd /local_home/share/trail-mapping/dry/a/csv
    for dat in 1d-* 2d-*
    do
        cd /local_home/share/trail-mapping
        gnuplot -e "set datafile separator ','; set terminal png size 800,600 enhanced font 'Helvetica,20'; set output 'combined_plots/$dat-all-bags-$part.png'; plot 'dry3/$part/csv/$dat' w d, 'wet/$part/csv/$dat' w d, 'dusk/$part/csv/$dat' w d, 'night3/$part/csv/$dat' w d"
    done

    cd /local_home/share/trail-mapping/dry/a/csv
    for dat in 3d-*
    do
        cd /local_home/share/trail-mapping
        gnuplot -e "set datafile separator ','; set terminal png size 800,600 enhanced font 'Helvetica,20'; set output 'combined_plots/$dat-all-bags-$part.png'; splot 'dry3/$part/csv/$dat' w d, 'wet/$part/csv/$dat' w d, 'dusk/$part/csv/$dat' w d, 'night3/$part/csv/$dat' w d"
    done
done

for bag in dry3 wet dusk night3
do
    gnuplot -e "set datafile separator ','; set terminal png size 800,600 enhanced font 'Helvetica,20'; set output 'combined_plots/3d-lat-long-alt-navsat_fix-a-b-$bag.png'; splot '$bag/a/csv/3d-lat-long-alt-navsat_fix.csv' w d, '$bag/b/csv/3d-lat-long-alt-navsat_fix.csv' w d"
    gnuplot -e "set datafile separator ','; set terminal png size 800,600 enhanced font 'Helvetica,20'; set output 'combined_plots/2d-lat-long-navsat_fix-a-b-$bag.png'; plot '$bag/a/csv/2d-lat-long-navsat_fix.csv' w d, '$bag/b/csv/2d-lat-long-navsat_fix.csv' w d"
done

rename -f 's/.csv//' combined_plots/*.png
