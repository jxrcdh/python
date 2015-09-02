ems_info_regex=r'\[\w+\s+?:(\d{2}:\d{2}:\d{2}\.\d+):\w+:\w+\[(\d+)\]:\d+:\d+\]==Ems:(\d+_\d+)\,Local\[(\d+)\]\s+\w+\[\w+\]\,side\[(\d{1})\]\,offset\[(\d{1})\].+$'
r_info_regex=r'\[\w+\s+?:(\d{2}:\d{2}:\d{2}\.\d+):\w+:\w+\[(\d+)\]:\d+:\d+\]R\s+(\d+)\s+(\d+)\s+(\d+).+$'
t_info_regex=r'\[\w+\s+?:(\d{2}:\d{2}:\d{2}\.\d+):\w+:\w+\[(\d+)\]:\d+:\d+\]T\s+(\d+)\s+(\d+).+$'
order_info_regex=r'\[\w+\s+?:(\d{2}:\d{2}:\d{2}\.\d+):\w+:\w+\[(\d+)\]:\d+:\d+\]==Order\s+Rsp:\s+(\d+_\d+)\,Local\[(\d+)\]\,Sys\[(\d+)\]\,\Create\[(\d+)\]\,Recv\[(\d+)\]\,Send\[(\d+)\]\,Over\[(\d+)\]\,Rsp\[(\d+)\]\,Sec\[(\d+)\].*$'
cancel_regex=r'\[\w+\s*:(\d{2}:\d{2}:\d{2}\.\d+):\w+:\w+\[(\d+)\]:\d+:\d+\]Cancel\s+Order:(\d+_\d+)\,Local\[(\d+)\]\,Sys\[(\d+)\].*$'
cancel_Rsp_regex=r'\[\w+\s*:(\d{2}:\d{2}:\d{2}\.\d+):\w+:\w+\[(\d+)\]:\d+:\d+\]Order\s+Rsp:\s+(\d+_\d+)\,Local\[(\d+)\]\,Sys\[(\d+)\]\,Status\[(\d+)\].*$'

