# -*- coding: utf-8 -*-

import logging
import time
from daemonize import Daemonize
import glob
import os

pid = "/tmp/timeTracking.pid"
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False
fh = logging.FileHandler("/tmp/timeTracking.log", "w")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
keep_fds = [fh.stream.fileno()]
actualPath = os.path.dirname(os.path.abspath(__file__))
filePathPrefix = actualPath + "/reports"

_lapse = 1800


def main(latest_file=None):
  savedTime = time.localtime(time.time())
  if (not latest_file):
    logger.debug("Creating new report file")
    filepath = "{}/{}-{}-{}_{}:{}.txt".format(filePathPrefix,savedTime.tm_mday,savedTime.tm_mon,
                                        savedTime.tm_year,savedTime.tm_hour,savedTime.tm_min)
    logger.debug("saving file on {}".format(filepath))
    with open(filepath, "w") as f:
      logger.debug(f)
      f.write("Time tracking for date {}".format(filepath))
  else:
    filepath = latest_file


  while True:
    code = os.system("python {}/timeTracker.py {}".format(actualPath,filepath))
    logger.debug("Exit code: {}".format(code))
    if (code == 512):
      daemon.close()
      break
    time.sleep(_lapse)

def rerun_process():
  


def start():
  is_running = os.path.isfile(pid) 
  if (is_running):
    logger.debug("Proccess already started, recovering...")
    list_of_files = glob.glob('{}/*.txt'.format(filePathPrefix))
    if (len(list_of_files) > 0):        
      latest_file = max(list_of_files, key=os.path.getctime)
      main(latest_file)
    exit(1)
  else:
    logger.debug("Time Tracking started...")
    daemon = Daemonize(app="time_tracking", pid=pid, action=main, keep_fds=keep_fds)
    daemon.start()

start()



