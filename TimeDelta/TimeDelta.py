#!/bin/python

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
    print t1 , " " , t2
    return int(t1)-int(t2)
    
if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        t1 = raw_input()

        t2 = raw_input()

        delta = time_delta(t1, t2)
