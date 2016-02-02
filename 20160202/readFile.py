# -*- coding:utf-8 -*-
# yield文件读取
def read_file(fpath):
	BLOCK_SIZE = 1024
	with open(fpath, 'rb') as f:
		while True:
			block = f.read(BLOCK_SIZE)
			if block:
				yield block
			else:
				return

if __name__ == '__main__':
	for res in read_file('E:/address.dmp'):
		print res