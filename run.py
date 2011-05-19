#!/usr/bin/python2.6
# -*- coding: utf-8 -*-

import era
import copy
import sys



output_vessel = []
file = open("exit.csv", "w")



def FilterContracts(keys):
  for era_contracts,era_path in era.output_era:
    contracts = {}
    for c,req in era_contracts.iteritems():
      skip = False
      for k,v in req.iteritems():
        if k in ['start', 'duration', 'revenue', 'color']:
          continue
        if type(v) == bool:
          if v and not (k in keys and keys[k]):
            skip = True
            continue

        else:
          assert k in keys, "missing key on Vessel (%s)" % k
          if keys[k] < v:
            skip = True
            continue
      if not skip:
        contracts[c] = req
    yield (era_path, contracts)

def PickRoute(contracts, pick, options):
  if not contracts:
    options.append(pick)
    return

  contracts_keys = contracts.keys()
  for i, ck in enumerate(contracts_keys):
    c = contracts[ck]
    newc = {}
    for k in contracts_keys[i+1:]:
      n = contracts[k]
      if (n['start'] >= c['start'] and
          n['start'] <= (c['start'] + c['duration'])):
        continue
      if ((n['start'] + n['duration']) >= c['start'] and 
          (n['start'] + n['duration']) <= (c['start'] + c['duration'])):
        continue
      if (n['start'] < c['start'] and 
          (n['start'] + n['duration']) > (c['start'] + c['duration'])):
        continue
      newc[k] = n
    PickRoute(newc, pick[:] + [ck], options)
    

def RevenueOf(contracts, path):
  return sum(contracts[x]['revenue'] for x in path) 

def Vessel(name, **keys):
  for era_path, contracts in FilterContracts(keys):
    final = []
    PickRoute(contracts, [], final)
    best_final = max(final, key=lambda p: RevenueOf(contracts, p))
    val = RevenueOf(contracts, best_final)
    print "Vessel:", name, "  Era:", era_path,"  Contract Path:", best_final, "  Revenue:", val, "  Profit:", val - keys['cost'], "  Cost:", keys['cost']
    output_vessel.append([name,era_path, best_final, val, val - keys['cost'],keys['cost']])
    csv_print =  ["Vessel,", name, ",  Revenue,", val, ",  Profit,", val - keys['cost'], ",  Cost:,", keys['cost'], ",  Era,", era_path,",  Contract Path,", best_final, "\n"]
      #print csv_print 
    for i in csv_print:
        file.write(str(i))

    
