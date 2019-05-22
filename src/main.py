# -*- coding: utf-8 -*-

import logging
import time
from daemonize import Daemonize
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

_lapse = 1800



def main():
    savedTime = time.localtime(time.time())
    logger.debug("Time Tracking started...")
    filepath = "{}/{}-{}-{}_{}:{}.txt".format(actualPath,savedTime.tm_mday,savedTime.tm_mon,
                                        savedTime.tm_year,savedTime.tm_hour,savedTime.tm_min)
    logger.debug("saving file on {}".format(actualPath + "/" + filepath))
    with open(filepath, "w") as f:
      f.write("Time tracking for date {}".format(filepath))

    while True:
      code = os.system("python {}/timeTracker.py {}".format(actualPath,filepath))
      logger.debug("Exit code: {}".format(code))
      if (code == 512):
        daemon.close()
        break
      time.sleep(_lapse)

    
    



daemon = Daemonize(app="time_tracking", pid=pid, action=main, keep_fds=keep_fds)
daemon.start()

