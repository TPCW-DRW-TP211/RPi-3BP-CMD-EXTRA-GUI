#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
import picamera

from tkinter import messagebox as msgbox
from time import sleep

def btn1_clicked():

                cgps -s

def btn2_clicked():

                camera = picamera.PiCamera()
                camera.capture('image.jpg')
 
                camera.start_preview()
                camera.vflip = True
                camera.hflip = True
                camera.brightness = 60
 
                camera.start_recording('video.h264')
                sleep(5)
                camera.stop_recording()

                top = tk.Tk()

top.title("终端命令菜单")

 

btn1 = tk.Button(top, text = "全球定位系统", command = btn1_clicked)

btn1.pack(fill = tk.X)

btn2 = tk.Button(top, text = "拍摄", command = btn2_clicked)

btn2.pack(fill = tk.X)

top.mainloop()
