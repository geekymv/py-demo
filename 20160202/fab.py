# -*-coding:utf-8 -*-
# python yield的使用
# http://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/

# 输出前n个斐波那契数列
#v1
def fab(n):
	i, a, b = 0, 0, 1
	while i < n:
		print b
		a, b = b, a + b
		i = i + 1
#v2
def fab2(n):
	i, a, b = 0, 0, 1
	res = []
	while i < n:
		res.append(b)
		a, b = b, a + b
		i = i + 1
	return res

# v3
class Fab(object):
	def __init__(self, n):
		self.n = n
		self.i, self.a, self.b = 0, 0, 1
	
	def __iter__(self):
		return self

	def next(self):
		if self.i < self.n:
			res = self.b
			self.a, self.b = self.b, self.a + self.b
			self.i = self.i + 1
			return res
		raise StopIteration()

def fab4(n):
	i, a, b = 0, 0, 1
	while i < n:
		yield b
		a, b =  b, a + b
		i = i + 1
			
if __name__ == '__main__':
	#print fab2(5)
	'''
	for n in Fab(5):
		print n
	
	print fab4(5)
	for n in fab4(6):
		print n
	'''
	from inspect import isgeneratorfunction
	print isgeneratorfunction(fab4)


