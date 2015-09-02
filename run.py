#!/usr/bin/env python
# -*- coding: utf-8 -*-
'Main Module of the program'

__author__ = 'donghao@wizardquant.com'

import read_and_split as rs
import info_process as ipr
import write_file as wf
from time import clock
import sys

args=sys.argv
if len(args) == 1:
	print 'need log file path'
elif len(args)==2:
	start=clock()
	infos=rs.read_log(args[1])
	finish=clock()
	print finish-start
else:
	print 'too many arguments'

notmatch_info = []
cancel_orders=[]
start=clock()
datas=ipr.process_strs(infos,notmatch_info,cancel_orders)
finish=clock()
print finish-start

print len(datas)

start=clock()
wf.write_err('notmatch_log.dat',notmatch_info)
wf.write_data_simple('cancel_orders.dat',cancel_orders)
finish=clock()
print finish-start

grouped_data=[]
data_dict={}
for info in datas:
	wf.group_data(data_dict,info,grouped_data)
start=clock()
for key in data_dict:
	wf.write_data(key+"_Orders.dat",grouped_data[data_dict[key]])
	print key,len(grouped_data[data_dict[key]])
finish=clock()
print finish-start
