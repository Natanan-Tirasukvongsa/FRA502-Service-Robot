# FRA502-Service-Robot
This robot is moving base (by differential drive) &amp; pick and plack (scala)

## Simulation Phase I
open first terminal and launch RVIZ by following this 

~~~~~~
$ roslaunch dd_sim dd_rviz.launch
~~~~~~

or launch RVIZ & Gazebo together

~~~
$ roslaunch dd_sim dd_gazebo.launch
~~~

open second terminal to show rostopic list

~~~
$ rostopic list
~~~

output will show 

~~~
/dd/camera1/image_raw
~~~
~~~
/dd/laser/scan
~~~

###open camera###

$ rosrun image_view image_view image:=/dd/camera1/image_raw

###output###

[ INFO] [1634705652.284265008]: Initializing nodelet with 4 worker threads.

[ INFO] [1634705652.431830628]: Using transport "raw"

#####third terminal#####

###control robot arm###

$ roslaunch dd_arm_control dd_control.launch

#####fourth terminal#####

###rostopic list ###

$ rostopic list

###main output###

/dd/joint1_position_controller/command

/dd/joint2_position_controller/command

### if no show main output###
$ rosservice call /dd/controller_manager/load_controller "name: 'joint1_position_controller'"

$ rosservice call /dd/controller_manager/load_controller "name: 'joint1_position_controller'"

### output ###

ok: True

###add input to control robot arm###

$ rostopic pub /dd/joint1_position_controller/command std_msgs/Float64 "data: 1.57"

$ rostopic pub /dd/joint2_position_controller/command std_msgs/Float64 "data: -0.7"

###output###

publishing and latching message. Press ctrl-C to terminate

#####fifth terminal#####

###control robot teleop###

$roslaunch dd_simple_control dd_control_teleop.launch

###follow keyboard on the screen###
