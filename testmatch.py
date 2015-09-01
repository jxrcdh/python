import re

regex=r'\[\w+\s+?:(\d{2}:\d{2}:\d{2}\.\d+):\w+:\w+\[(\d+)\]:\d+:\d+\]R\s+(\d+)\s+(\d+)\s+(\d+).+$'
str='[INFO  :15:04:12.847396:LOG_EMS:Ems[9990011112]:7635:21192]R 888 121 302506 54252839395'
infos=str.split(']')
print len(infos)
