# -*- coding:utf-8 -*-
import threading

def func():
	print 'hello timer'

# 用于在指定时间后调用一个方法
timer = threading.Timer(5, func)
timer.start()