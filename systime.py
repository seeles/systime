#-*- coding:utf-8 -*- 


import time 
import win32api 


def setSystemTime(direction):
	if direction == 17:
		tm_year = 2017
		tm_mon = 1
		tm_mday = 21
		tm_hour = 0
		tm_min =0
		tm_sec = 0 
		tm_wday = 6
		tm_yday = 21 
		tm_isdst = -1
		win32api.SetSystemTime(tm_year, tm_mon, tm_wday, tm_mday, tm_hour, tm_min, tm_sec, 0) 
		print "Set System OK!"
	if direction == 18:
		tm_year = 2018
		tm_mon = 1
		tm_mday = 21
		tm_hour = 0
		tm_min =0
		tm_sec = 0 
		tm_wday = 6
		tm_yday = 21 
		tm_isdst = -1
		win32api.SetSystemTime(tm_year, tm_mon, tm_wday, tm_mday, tm_hour, tm_min, tm_sec, 0) 
		print "Set System OK!"

direction = int(input('2017-->17 or 2018-->18:'))
print direction
setSystemTime(direction)