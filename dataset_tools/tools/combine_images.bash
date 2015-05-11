#! /bin/bash

echo "creating composite images with 2pix border"
./border_combine_images.bash 2 combined

echo "creating composite images with no border"
./border_combine_images.bash 0 combined_noborder
