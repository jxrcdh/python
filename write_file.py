def write_data(path,infos):
	f=open(path,'w')
	offsets=map(getoffset,infos)
	sides=map(getside,infos)
	tinfos=map(gett,infos)
	f.write('record:'+str(len(infos))+'\tsides:'+str(sum(sides))+'\toffsets:'+str(sum(offsets))+'\tT:'+str(sum(tinfos))+'\n')	
	for info in infos:
		for splitstr in info:
			f.write(splitstr+'\t')
		f.write('\n')
def write_err(path,infos):
	f=open(path,'w')
	for info in infos:
		f.write(info+'\n')
def getoffset(v):
	if len(v)>=5:
		return int(v[4])
	else:
		return 0
def getside(v):
	if len(v)>=4:
		return int(v[3])
	else:
		return 0
def gett(v):
	if len(v)>=8:
		return int(v[7])
	else:
		return 0
