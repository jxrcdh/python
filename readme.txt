This is a exercise to process the log file
In the ems.log file there are many trade information
a order with start of ==Ems:XX Local:XX
and a message ==Order or a R message
and end with T message
the Order message constract with Ems with Local and emsno
the R message constract with ems with emsno
the T message constract with R with a number.

The job of the program is to fetch the orders and count the offset and side
col

to run the program use command: python run.py
a file named processed_log.dat will generate to log the order
a file named notmatch_log.dat will generate to log the a no completed order
