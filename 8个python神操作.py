# D:\Users\Administrator\Anaconda3\python.exe
# -*- coding: utf-8 -*-
# @File  : 8个python神操作.py
# @Author: zhu
# @Date  : 2019-09-13tt
# 1  print打印带有颜色的信息
# •设置格式：033[显示方式;前景色;背景色 m

def esc(code=0):
    return f'\033[{code}m'


print(esc('31;1;0') + 'Error:' + esc() + 'important')

# 2、实现一个进度条

from time import sleep


def progess(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']', f' {percent:.0f}%', sep='', end='', flush=True)
    """
    上面的代码中的 print 有几个有用的参数，sep 的作用是已什么为分隔符，默认是空格，这里设置为空串是为了让每个字符之间更
    紧凑,end 参数作用是已什么结尾，默认是回车换行符，这里为了实现进度条的效果，同样设置为空串。还有最后一个参数 flush，
    该参数的作用主要是刷新， 默认 flush = False，不刷新，print 到 f 中的内容先存到内存中；而当 flush = True 时它会立即把
    内容刷新并输出
    """


for i in range(101):
    progess(i)
    sleep(0.1)

# 3、优雅打印嵌套类型的数据
import json
from pprint import pprint

str = {"status": "OK", "count": 2, "results": [{"age": 27, "name": "Oz", "lactose_intolerant": "1"},
                                               {"age": 29, "name": "Joe", "lactose_intolerant": "0"}]}
print(json.dumps(str, indent=2))
print('=' * 80)
pprint(str, width=2)

x = None  # type: List[str]
