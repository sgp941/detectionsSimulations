#!/bin/sh
export LD_LIBRARY_PATH=~/Documents/opencv-2.4.10/release/lib:$LD_LIBRARY_PATH

./CRForest-Detector 0 example/config.txt

