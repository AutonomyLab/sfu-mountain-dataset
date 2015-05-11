#! /bin/zsh

#for bag in dry3 wet dusk night3
#do
#    for part in a b
#    do
#        mkdir -p histograms/${bag}-$part/
#        echo "making plots for $bag - $part"
#        cd $bag/$part/csv
#        for csv in 1d-*.csv
#        do
#            if [[ $csv =~ "seq-stamp" ]]
#            then
#                :
#            else
#                #name=$csv xname=$csv yname="count" datafile=$csv outfile=${csv}-plot.png ../../../histogram.gnuplot
#            fi
#        done
#        mv *.png ../../../histograms/${bag}-$part/
#        cd ../../..
#    done
#done

for part in a b
do
    echo "making select aggregation plots for part $part"

    mkdir -p histograms

    cat dry3/$part/csv/1d-ax-imu_data.csv wet/$part/csv/1d-ax-imu_data.csv dusk/$part/csv/1d-ax-imu_data.csv night3/$part/csv/1d-ax-imu_data.csv > /tmp/temp.csv
    xname="x acceleration ({/Helvetica-Italic m/s^2})" datafile="/tmp/temp.csv" outfile="histograms/ax-$part.png" ./histogram.gnuplot

    cat dry3/$part/csv/1d-pitch-imu_data.csv wet/$part/csv/1d-pitch-imu_data.csv dusk/$part/csv/1d-pitch-imu_data.csv night3/$part/csv/1d-pitch-imu_data.csv > /tmp/temp.csv
    xname="pitch ({/Helvetica-Italic rad})" datafile="/tmp/temp.csv" outfile="histograms/pitch-$part.png" ./histogram.gnuplot

    cat dry3/$part/csv/1d-roll-imu_data.csv wet/$part/csv/1d-roll-imu_data.csv dusk/$part/csv/1d-roll-imu_data.csv night3/$part/csv/1d-roll-imu_data.csv > /tmp/temp.csv
    xname="roll ({/Helvetica-Italic rad})" datafile="/tmp/temp.csv" outfile="histograms/roll-$part.png" ./histogram.gnuplot

    cat dry3/$part/csv/1d-yaw-imu_data.csv wet/$part/csv/1d-yaw-imu_data.csv dusk/$part/csv/1d-yaw-imu_data.csv night3/$part/csv/1d-yaw-imu_data.csv > /tmp/temp.csv
    xname="yaw ({/Helvetica-Italic rad})" datafile="/tmp/temp.csv" outfile="histograms/yaw-$part.png" ./histogram.gnuplot

    #cat dry3/$part/csv/1d-pressure-barometric_pressure.csv wet/$part/csv/1d-pressure-barometric_pressure.csv dusk/$part/csv/1d-pressure-barometric_pressure.csv night3/$part/csv/1d-pressure-barometric_pressure.csv > /tmp/temp.csv
    cat dry3/$part/csv/1d-pressure-barometric_pressure.csv > /tmp/temp.csv
    xname="pressure ({/Helvetica-Italic Pa})" datafile="/tmp/temp.csv" outfile="histograms/pressure-$part.png" ./pressure-hist.gnuplot

    cat dry3/$part/csv/1d-vx-encoder.csv wet/$part/csv/1d-vx-encoder.csv dusk/$part/csv/1d-vx-encoder.csv night3/$part/csv/1d-vx-encoder.csv > /tmp/temp.csv
    xname="x velocity ({/Helvetica-Italic m/s})" datafile="/tmp/temp.csv" outfile="histograms/vx-$part.png" ./vel-hist.gnuplot

    cat dry3/$part/csv/1d-vyaw-encoder.csv wet/$part/csv/1d-vyaw-encoder.csv dusk/$part/csv/1d-vyaw-encoder.csv night3/$part/csv/1d-vyaw-encoder.csv > /tmp/temp.csv
    xname="angular velocity ({/Helvetica-Italic rad/s})" datafile="/tmp/temp.csv" outfile="histograms/vyaw-$part.png" ./histogram.gnuplot

    cat dry3/$part/csv/1d-alt-navsat_fix.csv > /tmp/temp.csv
    #cat dry3/$part/csv/1d-alt-navsat_fix.csv wet/$part/csv/1d-alt-navsat_fix.csv dusk/$part/csv/1d-alt-navsat_fix.csv night3/$part/csv/1d-alt-navsat_fix.csv > /tmp/temp.csv
    xname="altitude ({/Helvetica-Italic m})" datafile="/tmp/temp.csv" outfile="histograms/alt-$part.png" ./alt-hist.gnuplot
done
