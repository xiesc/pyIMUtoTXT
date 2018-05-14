# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 14:07:07 2018

@author: xiesc
"""
#%%
import rospy
import rosbag

#%%
bagpath = '/media/xiesc/Xie Shichao/北汽标定/lidar_gps_calibration/' 
bagname = '2018-04-10-19-36-00.bag'
bag = rosbag.Bag(bagpath+bagname)
with open(bagpath+bagname.split('.')[0]+'imu.txt','w') as f:
    for topic,msg,t in bag.read_messages(topics=['/imu/data']):
         f.write(str(t.secs)+'.'+str(t.nsecs))
         f.write(' ')
         f.write(str(msg.orientation.x))
         f.write(' ')
         f.write(str(msg.orientation.y))
         f.write(' ')
         f.write(str(msg.orientation.z))
         f.write(' ')
         f.write(str(msg.orientation.w))
         f.write('\n')

with open(bagpath+bagname.split('.')[0]+'gps.txt','w') as f:
    for topic,msg,t in bag.read_messages(topics=['/gps/fix']):
         f.write(str(t.secs)+'.'+str(t.nsecs))
         f.write(' ')
         f.write(str(msg.longitude))
         f.write(' ')
         f.write(str(msg.latitude))
         f.write(' ')
         f.write(str(msg.altitude))
         f.write('\n')
bag.close()
