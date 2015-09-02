import sys
import read_and_split as rs
import StrClass as sc
from time import clock

args=sys.argv
infos=[]
if len(args) == 1:
	print 'need log file path'
elif len(args)==2:
	start=clock()
	infos=rs.read_log(args[1])
	finish=clock()
	print finish-start
else:
	print 'too many arguments'

start=clock()
l=sc.test(infos)
finish=clock()
print finish-start
print len(l)
