# -*- coding:utf-8 -*-

names = ['Alice', 'Beth', 'Bob', 'Cecil']
numbers = ['2341', '9102', '0142', '5551']

#print names.index('Bob')
print numbers[names.index('Bob')]


phonebook = {'Alice': '2341'}
print phonebook['Alice']

# 将值关联到键上
phonebook['Bob'] = '1234'

print '字典中项的数量 ', len(phonebook)
