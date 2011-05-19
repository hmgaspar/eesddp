#!/Library/Frameworks/Python.framework/Versions/Current/bin/python
# -*- coding: utf-8 -*-

from era import *





Contract("Brazil 1", start=2011, duration=5, revenue=5,
         complex=3, color = (0.57,0.79,0.86))
Contract("Brazil 2", start=2013, duration=3, revenue=10,
        complex=5, color = (0.57,0.79,0.86))
Contract("Brazil 3", start=2014, duration=2, revenue=4,
         complex=2, color = (0.57,0.79,0.86))
Contract("Brazil 4", start=2017, duration=4, revenue=8,
         complex=2, color = (0.57,0.79,0.86))
Contract("Brazil 5", start=2016, duration=4, revenue=8,
         complex=3, color = (0.57,0.79,0.86))


# roubadinha do tempo pra eventos dependentes.
"""
for i in range(3):
  def func(a):
    @Uncertainty("Add t%i"  %i,t=i)
    def f():
      Contract("Random %i"%i , start=2011+i, duration=5, revenue=i ,
               complex=i, color = (i/10.0,0.79,i/10.0))
  func(i)
"""

#eventos independentes

for i in range(4):
    @Uncertainty("Add Africa t = %i"%i, t=0)
    def f():
        Contract("Africa %i"%i, start=2011+i, duration=i, revenue=7,
             complex=4, color = (1,0.79,0.86))


#@Uncertainty("Add Africa", t=0)
def f():
    Contract("Africa 1", start=2014, duration=7, revenue=7,
             complex=4, color = (1,0.79,0.86))
    Contract("Africa 2", start=2012, duration=9, revenue=8,
         complex=3, color = (1,0.79,0.86))
    Contract("Africa 3", start=2017, duration=4, revenue=8,
         complex=4, color = (1,0.79,0.86))
    Contract("Africa 4", start=2011, duration=3, revenue=5,
         complex=4, color = (1,0.79,0.86))
    Contract("Africa 5", start=2013, duration=3, revenue=5,
         complex=3, color = (1,0.79,0.86))
    del contracts['Brazil 1']
    del contracts['Brazil 2']
    del contracts['Brazil 3']
    del contracts['Brazil 4']
    del contracts['Brazil 5']

#@Uncertainty("Africa + Brazil", t=4)
def f():
    Contract("Africa 1", start=2014, duration=7, revenue=7,
             complex=4, color = (1,0.79,0.86))
    Contract("Africa 2", start=2012, duration=9, revenue=8,
             complex=3, color = (1,0.79,0.86))
    Contract("Africa 3", start=2017, duration=4, revenue=8,
             complex=4, color = (1,0.79,0.86))
    Contract("Africa 4", start=2011, duration=3, revenue=5,
             complex=4, color = (1,0.79,0.86))
    Contract("Africa 5", start=2013, duration=3, revenue=5,
             complex=3, color = (1,0.79,0.86))


#@Uncertainty("Add Norway", t=4)
def f():
  Contract("Norway 1", start=2015, duration=5, revenue=10,
           complex=5, ic=True, color = (0.57,0.79,1))
  Contract("Norway 2", start=2017, duration=3, revenue=7,
             complex=5, ic=True, color = (0.57,0.79,1))
  Contract("Norway 3", start=2015, duration=2, revenue=10,
         complex=5, ic=True, color = (0.57,0.79,1))

#@Uncertainty("delete contract 1", t=1)
def f():
  del contracts['Brazil 1']


#@Uncertainty("autonomy", t=1)
def f():
  contracts['Contract 7']['auton'] = 10

Compute()

print "Solution"
run.Vessel("A", cost=5, complex=3)
run.Vessel("B", cost=7, complex=4)
run.Vessel("C", cost=10, complex=5)
run.Vessel("D", cost=15, complex=5, ic=True)
run.Vessel("E", cost=4, complex=2)
"""
for i in range(100):
    run.Vessel(i, cost = i, complex = i)
"""
    
plot.Plot()


