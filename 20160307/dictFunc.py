#-*-coding:utf-8-*-

d = {}

# 如果试图访问字典中不存在的项时会报错，而get不会
#print d['name']
print d.get('name')
print d.get('name', 'default value') # 自定义默认值

