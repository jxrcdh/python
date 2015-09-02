def infoget(str1):
	substr=str1[24:31]
	if substr != 'LOG_EMS':
		return 'q'
	idx=findn(']',str1,2)
	if idx>=0:
		nextidx=idx+1
		if nextidx<len(str1) and str1[nextidx] in mes_type:
			if str1[nextidx] == '=':
				if (nextidx+1)<len(str1) and str1[nextidx+1] == 'E':
					return get_ems(re_dict['E'],str1)
				elif (nextidx+1)<len(str1) and str1[2] == 'O':
					return get_order(re_dict['O'],str1)
				else:
					return 'q'
			else:
				return mes_type[substr[0]](re_dict[substr[0]],str1)
		else:
			return 'q'
	else:
		return 'q'
mes_type={'=':1,'R':2,'T':3}
def test(infos):
	li=[]	
	for info in infos:
		p=infoget(info)
		li.append(p)
	print len(li)
	return li
def findn(substr,str1,n):
	sidx=0
	while n > 0:
		idx=str1.find(substr,sidx)
		if idx<0:
			return idx
		n=n-1
		sidx=idx
	return sidx
