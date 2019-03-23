#!/bin/python

import math
import os
import random
import re
import sys
import calendar

def formatToSec ( unFormatedTime ):
    totalseconds = 0
    TimeList = list(unFormatedTime)
    totalseconds = 36000 * int(TimeList[1]) + 3600 * int(TimeList[2]) + 600 * int(TimeList[3]) + 60 * 36000 * int(TimeList[4])
    if TimeList[1] == "-":
        return totalseconds * -1
    return totalseconds

def dayCount (unFormatedTime):
    totalDays = 


# Complete the time_delta function below.
#Sun 10 May 2015 13:54:36 -0000 parse this
def time_delta(t1, t2):
    time1 = t1.split()[-1]
    time2 = t2.split()[-1]
    #print time1 , " " , time2
    sectime1 = formatToSec(time1)
    sectime2 = formatToSec(time2)
    print abs(sectime1 - sectime2)
    # return int(t1)-int(t2)
    
    
if __name__ == '__main__':
    # t = int(raw_input())

    # for t_itr in xrange(t):
    #     t1 = raw_input()
    # Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000

    #     t2 = raw_input()s
    t1 = "Sat 02 May 2015 19:54:36 +0530"
    t2 = "Fri 01 May 2015 13:54:36 -0000"
    time_delta(t1, t2)
