# -*-coding:utf-8-*-

# 使用字典格式化字符串，%字符后面可以加上（用圆括号括起来的）键，
# 后面再跟上其他说明元素

phonebook = {'Alice': '2341'}
print '%(Alice)s' % phonebook

# 模板替换
template = '''<html>
			<head><title>%(title)s</title></head>
			<body>%(text)s</body>
		</html>
		'''
data = {'title': 'My Home Page', 'text': 'content'}
print template % data