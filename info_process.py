import re
def infoget(str):
	splitstr=str.split(']')
	if len(splitstr)>=3:
		substr = splitstr[2]
		if len(substr)>0 and substr[0] in mes_type:
			if substr[0] == '=':
				if substr[2] == 'E':
					return get_ems(str)
				else:
					return get_order(str)
			else:
				return mes_type[substr[0]](str);
		else:
			return ['q']
	else:
		return ['q']
def get_ems(str):
	m=re.match(ems_info_regex,str)	
	return ['e',m.group(1),m.group(3),m.group(4),m.group(5),m.group(6)]
def get_r_info(str):
	m=re.match(r_info_regex,str)
	if m is None:
		return ['q']
	else:
		return ['r',m.group(3),m.group(4),m.group(5)]
def get_t_info(str):
	m=re.match(t_info_regex,str)
	if m is None:
		return ['q']	
	else:
		return ['t',m.group(3),m.group(4)]
def get_order(str):
	m=re.match(order_info_regex,str)
	return ['o',m.group(3),m.group(4)]
mes_type={'=':get_ems,'R':get_r_info,'T':get_t_info}
ems_info_regex=r'\[\w+\s+?:(\d{2}:\d{2}:\d{2}\.\d+):\w+:\w+\[(\d+)\]:\d+:\d+\]==Ems:(\d+_\d+)\,Local\[(\d+)\]\s+\w+\[\w+\]\,side\[(\d{1})\]\,offset\[(\d{1})\].+$'
r_info_regex=r'\[\w+\s+?:(\d{2}:\d{2}:\d{2}\.\d+):\w+:\w+\[(\d+)\]:\d+:\d+\]R\s+(\d+)\s+(\d+)\s+(\d+).+$'
t_info_regex=r'\[\w+\s+?:(\d{2}:\d{2}:\d{2}\.\d+):\w+:\w+\[(\d+)\]:\d+:\d+\]T\s+(\d+)\s+(\d+).+$'
order_info_regex=r'\[\w+\s+?:(\d{2}:\d{2}:\d{2}\.\d+):\w+:\w+\[(\d+)\]:\d+:\d+\]==Order\s+Rsp:\s+(\d+_\d+)\,Local\[(\d+)\].+$'
def process_strs(infos,notmatch):
	index=-1
	savedata=[]
	for str in infos:
		datas=infoget(str)
		if datas[0] == 'e':
			datas.append('1')
			savedata.append(datas[1:7])
			index=index+1	
		elif datas[0] == 'r':
			reid = datas[1]+'_'+datas[2]
			beforeindex = index
			while beforeindex>=0:
				if reid == savedata[beforeindex][1] and savedata[beforeindex][5] == '1':
					savedata[beforeindex].append(datas[3])
					savedata[beforeindex][5]='3'
					break				
				beforeindex=beforeindex-1
			if beforeindex < 0:
				notmatch.append(str)
		elif datas[0] == 't':
			beforeindex = index
			while beforeindex>=0:
				if len(savedata[beforeindex])>=7 and savedata[beforeindex][6] == datas[1] and savedata[beforeindex][5] == '3':
					savedata[beforeindex].append(datas[2])
					savedata[beforeindex][5]='4'
					break				
				beforeindex=beforeindex-1
			if beforeindex < 0:
				notmatch.append(str)
		elif datas[0] == 'o':
			beforeindex = index
			while beforeindex>=0:
				if savedata[beforeindex][1] == datas[1] and savedata[beforeindex][2] == datas[2]:
					break				
				beforeindex=beforeindex-1
			if beforeindex < 0:
				notmatch.append(str)
		else:
			zhanwei=[]
			#print 'nouse'
	return savedata
