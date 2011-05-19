#!/usr/bin/python2.6
# -*- coding: utf-8 -*-

from era import *

Contract("Contract 1", start=0, duration=5, revenue=1e6,
         auton=17, capacity=3)
Contract("Contract 2", start=0, duration=3, revenue=2e6,
         auton=17, capacity=5)
Contract("Contract 3", start=3, duration=2, revenue=2e6,
         auton=14, capacity=5, depth=4)
Contract("Contract 4", start=3, duration=7, revenue=2e6,
         auton=14, capacity=5, depth=4)
Contract("Contract 5", start=1, duration=9, revenue=2e6,
         auton=14, capacity=5, depth=4)
Contract("Contract 6", start=6, duration=4, revenue=2e6,
         auton=14, capacity=5, depth=4)
Contract("Contract 7", start=7, duration=3, revenue=2e6,
         auton=14, capacity=5, depth=4)

"""


@Uncertainty("add", t=1)
def f():
  Contract("Contract 8", start=3, duration=2, revenue=3e6,
           range=13, capacity=4)

@Uncertainty("delete contract 1", t=1)
def f():
  del contracts['Contract 1']
"""
@Uncertainty("autonomy", t=1)
def f():
  contracts['Contract 7']['auton'] = 10



Compute()


