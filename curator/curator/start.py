#!/bin/python
import schedule
import time
import subprocess

## prod
def runcmd(cmd):
  return subprocess.call(cmd, shell=True)

## job group
def job_test():
  runcmd("sh /apps/test.sh")

def job_curator():
  rs = runcmd("sh /apps/cron.sh")


schedule.every(1).seconds.do(job_test)

while True:
  schedule.run_pending()
  time.sleep(1)
