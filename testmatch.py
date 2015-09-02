import re

regex=r'\[\w+\s*:(\d{2}:\d{2}:\d{2}\.\d+):\w+:\w+\[(\d+)\]:\d+:\d+\]Order\s+Rsp:\s+(\d+_\d+)\,Local\[(\d+)\]\,Sys\[(\d+)\]\,Status\[(\d+)\].*$'
str1='[INFO  :09:47:15.975390:LOG_EMS:Ems[9990011116]:11251:898]Order Rsp: 9_207,Local[135],Sys[517390],Status[5]'
m=re.match(regex,str1)
print m.group(1)
print m.group(2)
print m.group(3)
print m.group(4)
print m.group(5)
print m.group(6)
#print m.group(7)
#print m.group(8)
#print m.group(9)
#print m.group(10)
#print m.group(11)
