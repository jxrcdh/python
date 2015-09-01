import re

regex=r'\[\w+\s+?:(\d{2}:\d{2}:\d{2}\.\d+):\w+:\w+\[(\d+)\]:\d+:\d+\]==Order\s+Rsp:\s+(\d+_\d+)\,Local\[(\d+)\]\,Sys\[(\d+)\]\,\Create\[(\d+)\]\,Recv\[(\d+)\]\,Send\[(\d+)\]\,Over\[(\d+)\]\,Rsp\[(\d+)\]\,Sec\[(\d+)\].*$'
str1='[INFO  :09:35:34.874570:LOG_EMS:Ems[9990011112]:7635:58]==Order Rsp: 888_1,Local[1],Sys[389500],Create[34534864480],Recv[34534864499],Send[34534864509],Over[34534864514],Rsp[34534874569],Sec[34532000]'
m=re.match(regex,str1)
print m.group(1)
print m.group(2)
print m.group(3)
print m.group(4)
print m.group(5)
print m.group(6)
print m.group(7)
print m.group(8)
print m.group(9)
print m.group(10)
print m.group(11)
