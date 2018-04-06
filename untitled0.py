# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 14:07:07 2018

@author: xiesc
"""
#%%
import rospy
import rosbag

#%%
bagpath = '/media/xiesc/Xie Shichao/calibration_sick_gps/' 
bagname = '2018-04-02-23-16-56.bag'
bag = rosbag.Bag(bagpath+bagname)
with open(bagpath+bagname.split('.')[0]+'imu','w') as f:
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

with open(bagpath+bagname.split('.')[0]+'gps','w') as f:
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
