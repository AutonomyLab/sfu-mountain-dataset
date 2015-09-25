#! /usr/bin/gnuplot

datafile=system("echo $datafile")
outfile=system("echo $outfile")

xname=system("echo $xname")
yname=system("echo $yname")
name=system("echo $name")

system("awk -F, '{print $2}' $datafile > /tmp/datafile")
system("make_alt_histogram.py /tmp/datafile > /tmp/histfile")
#
#stats '/tmp/datafile'
#lower=STATS_min_y
#upper=STATS_max_y
#stride=(upper-lower)/40
#
#test_div_by_zero=1/(upper-lower)

stats "/tmp/histfile" nooutput

clear
reset
set key off
set border 15
set auto
 
unset x2tics
unset y2tics
set nox2tics
set noy2tics

ourxrange=300
ouryrange=STATS_max_y-STATS_min_y

set xrange [20:330] reverse
set yrange [STATS_min_y:STATS_max_y+ouryrange/10]

#set xtics stride*6
set format x "%.1f"
set xtics 40,(315-40)/4,315
set format y ""
set ytics STATS_min_y,int(int(STATS_max_y/4)/100)*100,STATS_max_y

#set noxtics
set xtics scale 0
set noytics

unset x2tics
unset y2tics
set nox2tics
set noy2tics

# Make some suitable labels.
#set title name
#set xlabel xname
#set ylabel yname
 
set terminal png linewidth 5 enhanced font Helvetica 32 size 800, 600
set output outfile
 
set style histogram clustered gap 1
set style fill solid border -1
 
#binwidth=stride
#set boxwidth binwidth
#bin(x,width)=width*floor(x/width) + binwidth/2.0

set cbrange [20:350]
set palette defined  (30 "#7f0000",\
                      70 "#ee0000",\
                      110 "#ff7000",\
                      150 "#ffee00",\
                      190 "#90ff70",\
                      230 "#0fffee",\
                      270 "#0090ff",\
                      310 "#000fff",\
                      350 "#000090")

unset colorbox

#set datafile separator ','
#plot "/tmp/datafile" using (bin($1,binwidth)):(1.0):(bin($1,binwidth)):(bin($1,binwidth)) smooth freq with boxes lc palette
plot "/tmp/histfile" using 1:2:1 with boxes lc palette
