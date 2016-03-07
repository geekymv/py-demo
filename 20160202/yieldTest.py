def cash_out(amount):
	while amount > 0:
		amount -= 1
		yield 1
		print 'cash out'

if __name__ == '__main__':
	for k in cash_out(5):
		print k