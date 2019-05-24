# coding: utf-8
# @Time    : 2019/5/24 15:37
# @Author  : AngDH


# 系统的内存利用率
import os
import time
from time import sleep

import psutil as psutil

# 系统的CPU利用率
# psutil.cpu_percent(None)

year = time.strftime("%Y", time.localtime())
mon = time.strftime("%m", time.localtime())
day = time.strftime("%d", time.localtime())
ymd = "%s%s%s" % (year, mon, day)
if not os.path.exists('c:/rec/'):
    # 如果 不存在 创建 文件夹
    os.makedirs('c:/rec/')


def start():
    print "监控内存与cpu开始"

    while True:
        # print psutil.virtual_memory().percent
        # print psutil.cpu_percent(None)
        s = "内存占用_%s" % psutil.virtual_memory().percent
        c = "cpu占用_%s" % psutil.cpu_percent(None)
        e = "%s_%s_%s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), s, c)
        with open('c:/rec/record_%s.txt' % (ymd), 'a') as f:
            f.write('\n%s' % (e))
        sleep(5)


if __name__ == '__main__':
    start()
