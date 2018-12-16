#!/bin/bash

# setup ros environment
source "/node-ws/devel/setup.bash"
export DUCKIEBOT_NAME=zjbot
#export ROS_MASTER_URI=http://zjbot.local:11311
roslaunch tf_sem_seg tf_sem_seg.launch veh:=$DUCKIEBOT_NAME
