# -*- coding: utf-8 -*-

import sys
import time
import os
import signal
from Tkinter import *

window = Tk()
window.title("Timetracker!")
window.geometry('300x300')
filepath = sys.argv[1]

if not filepath: exit(3)


def write(file, str):
  file.write("\n{}".format(str))

def onClick():
  toWrite=input.get() if len(input.get()) > 0 else lastTask
  timestruc = time.localtime(time.time())
  toWrite += ",     {}-{}-{} {}:{}hs".format(timestruc.tm_mday,timestruc.tm_mon,
                                        timestruc.tm_year,timestruc.tm_hour,timestruc.tm_min)
  if toWrite:
    write(f,toWrite)
    exit(0)

def onFinish() :
  exit(2)

def onReturn(event=None):
  if event:
    onClick()

window.bind('<Return>', onReturn)

with open(filepath, "a+") as f:

  message = StringVar()
  messageLabel = Label(window, textvariable=message)
  messageLabel.pack()

  lines = 0
  for l in f:
    lines += 1
    lastLine = l

  toWrite = ''

  if lines < 2:
    message.set("Input task name:")
  else:
    lastTask = lastLine.split(',')[0]
    message.set("Leave empty for re-use last task: \n\n{} \n\nOr Write new task:\n".format(lastTask))

  input = Entry( window,bd =5)
  input.pack()
  input.focus()




  button = Button(window, text ="Ok", command = onClick)
  button.pack()

  button = Button(window, text ="Terminar", command = onFinish)
  button.pack()

  


  window.mainloop()




  
