# -*- coding:utf-8 -*-
import pickle, json
data = {'k1': 123, 'k2': {'k22': 22, 'k23': 123}}
# 将数据通过特殊的形式转换为只有python语言人数的字符串
#res = pickle.dumps(data)
#print res

print json.dumps(data, sort_keys=True, indent=2)

