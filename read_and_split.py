def read_log(path):
	f=open(path,'r')
	text=f.read()
	infos=text.split('\n')
	return infos

