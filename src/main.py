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
latest_file= ''

_lapse = 1800


def main(reportFile=None):
  savedTime = time.localtime(time.time())
  logger.debug("sdfsdfsd{}".format(reportFile))
  if (not reportFile):
    logger.debug("Creating new report file")
    filepath = "{}/{}-{}-{}_{}:{}.txt".format(filePathPrefix,savedTime.tm_mday,savedTime.tm_mon,
                                        savedTime.tm_year,savedTime.tm_hour,savedTime.tm_min)
    logger.debug("saving file on {}".format(filepath))
    with open(filepath, "w") as f:
      logger.debug(f)
      f.write("Time tracking for date {}".format(filepath))
  else:
    filepath = reportFile


  while True:
    code = os.system("python {}/timeTracker.py {}".format(actualPath,filepath))
    if (code == 512):
      daemon.close()
      break
    time.sleep(_lapse)


def start():
  try:
    pidFile = open(pid)
    procces_id = pidFile.read().replace('%','')
    pidFile.close()
    is_running = os.system("kill -0 {}".format(procces_id))
    if (is_running == 0):
      logger.debug("Proccess already started, recovering...")

      os.system("kill -9 {}".format(procces_id))
      os.remove(pid)

      list_of_files = glob.glob('{}/*.txt'.format(filePathPrefix))
      if (len(list_of_files) > 0):        
        latest_file = max(list_of_files, key=os.path.getctime)
        logger.debug(latest_file)
        logger.debug("Using report file: {}".format(latest_file))
        def rerun() :
          main(reportFile=latest_file)
        daemon = Daemonize(app="time_tracking", pid=pid, action=rerun, keep_fds=keep_fds)
        daemon.start()
      exit(1)

  except Exception:
    logger.debug("Time Tracking started...")
    daemon = Daemonize(app="time_tracking", pid=pid, action=main, keep_fds=keep_fds)
    daemon.start()

start()



