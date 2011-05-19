#!/usr/bin/python2.6
# -*- coding: utf-8 -*-

import sys
import copy

import run
import plot

contracts = {}
uncertainty = {}
output_era = []
output_epoca = []
era_size = 10

def Contract(name, **keys):
  global contracts
  assert 'start' in keys
  assert 'duration' in keys
  contracts[name] = keys


def Uncertainty(name, t):
  def dec(f):
    uncertainty[name] = { 'time': t,
                          'func': f }
    return None
  return dec


def Call(c, f):
  global contracts
  orig_c = contracts.copy()
  contracts.clear()
  contracts.update(c)
  f()
  c = copy.deepcopy(contracts)
  contracts.clear()
  contracts.update(orig_c)
  return c


def OutputEra(c, p):
  print "-"*50
  print "Era", p
  for x in c:
    print "  ", x, c[x]
  output_era.append((copy.deepcopy(c), p[:]))
  
def OutputEpoca(begin, end, c, p):
  print "Epoch (%d, %d) %s:" % (begin, end, p), c.keys()
  output_epoca.append((begin, end, copy.deepcopy(c), p[:]))

def Progress(c, u, p, last_time):
  """
  c: contratos
  u: incertezas
  p: certezas
  last_time: instante a partir do qual estamos considerando

  """

  # Se nao tiver incerteza sobrando.
  # Primeiro valor the last time e' o tamanho total
  if not u:
    OutputEpoca(last_time, era_size, c, p)
    return OutputEra(c, p)

  # pega a incerteza mais proxima.
  initial_time = min(u[x]['time'] for x in u)
  OutputEpoca(last_time, initial_time, c, p)

  # Separa incertezas entre as que vao acontecer agora
  # e as seguintes.
  available = {}
  rest = {}
  for k in u:
    if u[k]['time'] == initial_time:
      available[k] = u[k]
    else:
      rest[k] = u[k]

  # adiciono nas incertezas que vao acontecer agora, nao acontecer nada.
  available[''] = { 'time': initial_time,
                    'func': lambda: None }

  # pra cada incerteza que vai ser aplicada.
  for k in available:
    # chamo a funcao da incerteza.
    new_c = Call(copy.deepcopy(c), available[k]['func'])
    # adiciona a incerteza na lista de incertezas aplicadas.
    new_p = p[:] + [k]
    # Chamo a progress de novo.
    Progress(new_c, rest, new_p, initial_time)


def Compute():
  Progress(contracts, uncertainty, [], 0)

