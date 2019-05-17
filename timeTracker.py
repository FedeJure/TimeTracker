# -*- coding: utf-8 -*-

import sys
import time
import os
import signal

filepath = sys.argv[1]

if not filepath: exit(3)

def getNewTask() :
  task =raw_input("Input task name:")
  return task

def getEntry(lastTask):
  entry = raw_input("press [Enter] for re-use last task: \n\n{} \n\nOr Write new task:\n".format(lastTask))
  return entry

def write(file, str):
  file.write("\n{}".format(str))

with open(filepath, "a+") as f:
  lines = 0
  for l in f:
    lines += 1
    lastLine = l

  toWrite = ''

  if lines < 2:
    task = getNewTask()
    toWrite = task
  else:
    lastTask = lastLine.split(',')[0]
    entry = getEntry(lastTask)
    if entry:
      toWrite = entry
    else:
      toWrite = entry = lastTask

  timestruc = time.localtime(time.time())
  toWrite += ",     {}-{}-{} {}:{}hs".format(timestruc.tm_mday,timestruc.tm_mon,
                                        timestruc.tm_year,timestruc.tm_hour,timestruc.tm_min)
  if toWrite:
    write(f,toWrite)
exit(0)