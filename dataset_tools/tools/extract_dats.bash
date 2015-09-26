#! /bin/bash

extract_encoder_vel_x.py < topics/encoder.topic > dat/encoder_vel_x.dat

extract_timeless_enu.py < topics/encoder.topic > dat/encoder_x_y.dat
extract_timeless_3d_odom.py < topics/encoder.topic > dat/encoder_3d.dat

extract_enu_x.py < topics/navsat_enu.topic > dat/navsat_enu_x.dat
extract_enu_y.py < topics/navsat_enu.topic > dat/navsat_enu_y.dat
extract_enu_z.py < topics/navsat_enu.topic > dat/navsat_enu_z.dat

#extract_enu_z.py < topics/pressure_odometry.topic > dat/pressure_z.dat
#extract_encoder_vel_z.py < topics/pressure_odometry.topic > dat/pressure_vel_z.dat

extract_gps_vel_heading.py < topics/navsat_vel.topic > dat/navsat_vel_theta.dat

extract_imu_orientation_x.py < topics/imu_data.topic > dat/imu_theta_x.dat
extract_imu_orientation_y.py < topics/imu_data.topic > dat/imu_theta_y.dat
extract_imu_orientation_z.py < topics/imu_data.topic > dat/imu_theta_z.dat

#extract_odom_heading.py < topics/odometry_filtered.topic > dat/odom_heading.dat
#extract_odom_orientation_x.py < topics/odometry_filtered.topic > dat/odom_theta_x.dat
#extract_odom_orientation_y.py < topics/odometry_filtered.topic > dat/odom_theta_y.dat
#extract_odom_orientation_z.py < topics/odometry_filtered.topic > dat/odom_theta_z.dat

extract_pressure.py < topics/barometric_pressure.topic > dat/pressure.dat

for i in topics/*
do
    extract_seq_stamp.py < $i > ${i/topics/dat}
done

extract_timeless_3d_gps.py < topics/navsat_fix.topic > dat/navsat_3d.dat
#extract_timeless_3d_odom.py < topics/odometry_filtered.topic > dat/odom_3d.dat
extract_timeless_3d_odom.py < topics/navsat_enu.topic > dat/navsat_enu_3d.dat
