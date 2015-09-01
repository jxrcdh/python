import read_and_split as rs
import info_process as ipr
import write_file as wf

infos=rs.read_log('ems.log')
notmatch_info = []
datas=ipr.process_strs(infos,notmatch_info)
print len(datas)
wf.write_data('processed_log.dat',datas)
wf.write_err('notmatch_log.dat',notmatch_info)
grouped_data=[]
data_dict={}
for info in datas:
	wf.group_data(data_dict,info,grouped_data)
for key in data_dict:
	print key,len(grouped_data[data_dict[key]])
