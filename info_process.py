import re
def infoget(str,re_dict):
	splitstr=str.split(']')
	if len(splitstr)>=3:
		substr = splitstr[2]
		if len(substr)>0 and substr[0] in mes_type:
			if substr[0] == '=':
				if substr[2] == 'E':
					return get_ems(re_dict['E'],str)
				elif substr[2] == 'O':
					return get_order(re_dict['O'],str)
				else:
					return ['q']
			else:
				return mes_type[substr[0]](re_dict[substr[0]],str)
		else:
			return ['q']
	else:
		return ['q']
count_re=0
def get_ems(reg,str):
	m=reg.match(str)
	global count_re
	count_re=count_re+1
	side='0'
	if m.group(5) >= '1':
		side='1'
	offset='0'
	if m.group(6) >= '1':
		offset='1' 
	return ['e',m.group(1),m.group(2),m.group(3),m.group(4),side,offset]
def get_r_info(reg,str):
	m=reg.match(str)
	global count_re
	count_re=count_re+1
	if m is None:
		return ['q']
	else:
		return ['r',m.group(3),m.group(4),m.group(5)]
def get_t_info(reg,str):
	m=reg.match(str)
	global count_re	
	count_re = count_re+1
	if m is None:
		return ['q']	
	else:
		return ['t',m.group(3),m.group(4)]
def get_order(reg,str):
	m=reg.match(str)
	global count_re	
	count_re = count_re+1
	if m is None:
		return ['q']
	else:
		return ['o',m.group(3),m.group(4),m.group(5),m.group(6),m.group(7),m.group(8)]
mes_type={'=':get_ems,'R':get_r_info,'T':get_t_info}
ems_info_regex=r'\[\w+\s+?:(\d{2}:\d{2}:\d{2}\.\d+):\w+:\w+\[(\d+)\]:\d+:\d+\]==Ems:(\d+_\d+)\,Local\[(\d+)\]\s+\w+\[\w+\]\,side\[(\d{1})\]\,offset\[(\d{1})\].+$'
r_info_regex=r'\[\w+\s+?:(\d{2}:\d{2}:\d{2}\.\d+):\w+:\w+\[(\d+)\]:\d+:\d+\]R\s+(\d+)\s+(\d+)\s+(\d+).+$'
t_info_regex=r'\[\w+\s+?:(\d{2}:\d{2}:\d{2}\.\d+):\w+:\w+\[(\d+)\]:\d+:\d+\]T\s+(\d+)\s+(\d+).+$'
order_info_regex=r'\[\w+\s+?:(\d{2}:\d{2}:\d{2}\.\d+):\w+:\w+\[(\d+)\]:\d+:\d+\]==Order\s+Rsp:\s+(\d+_\d+)\,Local\[(\d+)\]\,Sys\[(\d+)\]\,\Create\[(\d+)\]\,Recv\[(\d+)\]\,Send\[(\d+)\]\,Over\[(\d+)\]\,Rsp\[(\d+)\]\,Sec\[(\d+)\].*$'
def process_strs(infos,notmatch):
	index=-1
	savedata=[]
	re_ems = re.compile(ems_info_regex)
	re_r = re.compile(r_info_regex)
	re_t = re.compile(t_info_regex)
	re_order = re.compile(order_info_regex)
	re_dict={'E':re_ems,'R':re_r,'T':re_t,'O':re_order}
	for str in infos:
		datas=infoget(str,re_dict)
		if datas[0] == 'e':
			datas.append('1')
			datas.append('')
			datas.append(0)
			savedata.append(datas[1:10])
			index=index+1	
		elif datas[0] == 'r':
			reid = datas[1]+'_'+datas[2]
			beforeindex = index
			while beforeindex>=0:
				if reid == savedata[beforeindex][2] and savedata[beforeindex][6] == '1':
					savedata[beforeindex][7]=datas[3]
					savedata[beforeindex][6]='3'
					break				
				beforeindex=beforeindex-1
			if beforeindex < 0:
				notmatch.append(str)
		elif datas[0] == 't':
			beforeindex = index
			while beforeindex>=0:
				if len(savedata[beforeindex])>=8 and savedata[beforeindex][7] == datas[1]:
					if len(savedata[beforeindex]) >= 9:
						savedata[beforeindex][8] = savedata[beforeindex][8]+int(datas[2])
						savedata[beforeindex][6]=4
					else:
						print 'error'
					break				
				beforeindex=beforeindex-1
			if beforeindex < 0:
				notmatch.append(str)
		elif datas[0] == 'o':
			beforeindex = index
			while beforeindex>=0:
				if savedata[beforeindex][2] == datas[1] and savedata[beforeindex][3] == datas[2]:
					savedata[beforeindex] = savedata[beforeindex]+datas[3:len(datas)]					
					break				
				beforeindex=beforeindex-1
			if beforeindex < 0:
				notmatch.append(str)
		else:
			zhanwei=[]
			#print 'nouse'
	print 'count',count_re
	return savedata
