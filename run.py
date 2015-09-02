import read_and_split as rs
import info_process as ipr
import write_file as wf
from time import clock
start=clock()
infos=rs.read_log('LogReader.log')
finish=clock()
print finish-start
notmatch_info = []
start=clock()
datas=ipr.process_strs(infos,notmatch_info)
finish=clock()
print finish-start

print len(datas)
start=clock()
wf.write_err('notmatch_log.dat',notmatch_info)
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
