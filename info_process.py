import re
import regexs
def infoget(str1,re_dict):
	substr=str1[24:31]
	if substr != 'LOG_EMS':
		return 'q'
	idx=findn(']',str1,2)
	if idx>=0:
		nextidx=idx+1
		if nextidx<len(str1) and str1[nextidx] in mes_type:
			if str1[nextidx] == '=':
				if (nextidx+2)<len(str1) and str1[nextidx+2] == 'E':
					return get_ems(re_dict['E'],str1)
				elif (nextidx+2)<len(str1) and str1[nextidx+2] == 'O':
					return get_order(re_dict['O'],str1)
				else:
					return 'q'
			else:
				return mes_type[str1[nextidx]](re_dict[str1[nextidx]],str1)
		else:
			return 'q'
	else:
		return 'q'
count_re=0
def findn(substr,str1,n):
	sidx=0
	while n > 0:
		idx=str1.find(substr,sidx)
		if idx<0:
			return idx
		n=n-1
		sidx=idx+1
	return sidx-1
def get_ems(reg,str):
	m=reg.match(str)
	side='0'
	if m.group(5) >= '1':
		side='1'
	offset='0'
	if m.group(6) >= '1':
		offset='1' 
	return ['e',m.group(1),m.group(2),m.group(3),m.group(4),side,offset]
def get_r_info(reg,str):
	m=reg.match(str)
	#print str
	if m is None:
		return ['q']
	else:
		return ['r',m.group(3),m.group(4),m.group(5)]
def get_t_info(reg,str):
	m=reg.match(str)
	#print str
	if m is None:
		return ['q']	
	else:
		return ['t',m.group(3),m.group(4)]
def get_order(reg,str):
	m=reg.match(str)
	if m is None:
		return ['q']
	else:
		return ['o',m.group(3),m.group(4),m.group(5),m.group(6),m.group(7),m.group(8)]
def get_cancel_info(reg,str):
	m=reg.match(str)
	if m is None:
		return 'q'
	else:
		return ['c',m.group(2),m.group(3),m.group(4),m.group(5)]
def get_cancel_rsp(reg,str):
	m=reg.match(str)
	if m is None:
		return 'q'
	else:
		return ['p',m.group(2),m.group(3),m.group(4),m.group(5),m.group(6)]

mes_type={'=':get_ems,'R':get_r_info,'T':get_t_info,'C':get_cancel_info,'O':get_cancel_rsp}
def process_strs(infos,notmatch,cancelOrders):
	index=-1
	savedata=[]
	re_ems = re.compile(regexs.ems_info_regex)
	re_r = re.compile(regexs.r_info_regex)
	re_t = re.compile(regexs.t_info_regex)
	re_order = re.compile(regexs.order_info_regex)
	re_cancel=re.compile(regexs.cancel_regex)
	re_cancel_rsp=re.compile(regexs.cancel_Rsp_regex)
	re_dict={'E':re_ems,'R':re_r,'T':re_t,'O':re_order,'C':re_cancel,'O':re_cancel_rsp}
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
		elif datas[0]=='c':
			datas.append('1')
			cancelOrders.append(datas[1:6])
		elif datas[0]=='p':
			beforeindex=len(cancelOrders)-1
			while beforeindex>=0:
				if cancelOrders[beforeindex][0] == datas[1] and cancelOrders[beforeindex][1] == datas[2] and cancelOrders[beforeindex][2] == datas[3] and cancelOrders[beforeindex][3] == datas[4] and len(datas)>=6:
					cancelOrders[beforeindex][4]=datas[5]
					break
				beforeindex=beforeindex-1
			if beforeindex<0:
				notmatch.append(str)
		else:
			zhanwei=[]
			#print 'nouse'
	return savedata
