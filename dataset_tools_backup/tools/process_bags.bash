#! /bin/bash

./make_csvs.bash dry3
./make_csvs.bash wet
./make_csvs.bash dusk
./make_csvs.bash night3

./make_plots.bash
./make_histograms.zsh
