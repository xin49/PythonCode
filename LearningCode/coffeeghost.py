import os
def main():
	print 'Hello World!'
	print "This is Alice's greeting."
	print 'This is Bob\'s greeting.'
	foo(5, 10)
	print '=' * 10
	print 'Current working directory is ' + os.getcwd()
	counter = 0
	counter += 1
	food = ['apples', 'oranges', 'cats']
	for i in food:
		print 'I like to eat ' + i
	print 'Count to ten:'
	for i in range(10):
		print i

def foo(param1, secondParam):
	res = param1 + secondParam
	print '%s plus %s is equal to %s' % (param1, secondParam, res)
	if res < 50:
		print 'foo'
	elif (res >= 50) and ((param1 == 42) or (secondParam == 24)):
		print 'bar'
	else:
		print 'moo'

if __name__ == '__main__':
	main()
	os.system('pause')
