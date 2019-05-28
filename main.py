#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from Tkinter import *           # 导入 Tkinter 库
import time
root = Tk()                     # 创建窗口对象的背景色
                                # 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)          #  创建两个列表组件
listb2 = Listbox(root)
for item in time:
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # 格式化成2016-03-20 11:45:39形式
  
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)
 
for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)
 
listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()                 # 进入消息循环
