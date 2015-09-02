def write_data(path,infos):
	f=open(path,'w')
	combine=map(getcombine,infos)
	tinfos=map(gett,infos)
	count_com=count_combine(combine)
	str_dict={0:'Time:',1:'ID',2:'Ems',3:'Local',4:'Side',5:'Offset',6:'State',7:'R_id',8:'T',9:'Sys',10:'Create',11:'Recv',12:'Send'}
	f.write('\tside\toffset\tsum\tsumT\n')
	f.write('\t0\t0\t'+str(count_com[0][0])+'\t'+str(count_com[1][0])+'\n')
	f.write('\t0\t1\t'+str(count_com[0][2])+'\t'+str(count_com[1][2])+'\n')
	f.write('\t1\t0\t'+str(count_com[0][1])+'\t'+str(count_com[1][1])+'\n')
	f.write('\t1\t1\t'+str(count_com[0][3])+'\t'+str(count_com[1][3])+'\n')	
	f.write('sum\t\t'+str(len(combine))+'\t\t'+str(sum(tinfos))+'\n')	
	for info in infos:
		index=0
		while index<len(info):
			f.write(str_dict[index]+'['+str(info[index])+']\t')
			index=index+1
		f.write('\n')
def write_err(path,infos):
	f=open(path,'w')
	for info in infos:
		f.write(info+'\n')
def write_data_simple(path,infos):
	f=open(path,'w')
	for info in infos:
		for d in info:
			f.write(str(d)+'\t')
		f.write('\n')
def count_combine(comb):
	res=[[0,0,0,0],[0,0,0,0]]
	for comb_data in comb:
		res[0][comb_data[0]+comb_data[1]*2] = res[0][comb_data[0]+comb_data[1]*2]+1
		res[1][comb_data[0]+comb_data[1]*2] = res[1][comb_data[0]+comb_data[1]*2]+comb_data[2]
	return res 
def getcombine(v):
	if len(v)>=9:
		return [int(v[4]),int(v[5]),int(v[8])]
	else:
		return []
def gett(v):
	if len(v)>=9:
		return int(v[8])
	else:
		return 0
def group_data(id_dict,infos,grouped_info):
	if infos[1] in id_dict:
		grouped_info[id_dict[infos[1]]].append(infos)
	else:
		index = len(grouped_info)
		id_dict[infos[1]] = index
		grouped_info.append([])
		grouped_info[index].append(infos)
