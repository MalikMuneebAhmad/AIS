#!/usr/bin/env python3
# coding: UTF-8
# **************************************************
# *** Mobility trace of Homesick Levy Walk (HLW) ***
# *** Program author: Akihiro Fujihara           ***
# *** Usage: python3 abm-hlw-trace.py            ***
# **************************************************

# modules
import matplotlib
matplotlib.use('TkAgg')
import pylab as PL
import random as RD
import numpy as NP
import math

# generate random seed
RD.seed()

# model parameters
populationSize = 1 # the number of walkers
collisionDistance = 4 # encounter distance
CDsquared = collisionDistance ** 2
scaling_exponent = 1.0 # Power exponent of the distance to the destination
wait_exponent = 1.5 # Power exponent of wating time
homesick_prob = 0.0 # 0 --> Levy walk, otherwise --> Homesick Levy Walk
#homesick_prob = 0.1 # 0 --> Levy walk, otherwise --> Homesick Levy Walk
move_speed = 1.0 # moving speed of walkers
width = [-50,50]  # System width
height = [-50,50] # System height

# PyCX init
def init():
  global time, agents, destination_trace_x_list, destination_trace_y_list

  time = 0
  destination_trace_x_list = []
  destination_trace_y_list = []
  agents = []
  for i in range(populationSize):
    initX = 0.0
    initY = 0.0
    # data structure: present_x, present_y, meeting_flag, destination_x, destination_y, state, angle, home_x, home_y, wait_interval
    newAgent = [initX, initY, 0, 0.0, 0.0, 'stop', 0.0, initX, initY, 0]
    agents.append(newAgent)
    destination_trace_x_list.append([0.0])
    destination_trace_y_list.append([0.0])

# PyCX draw
def draw():
  global time, agents

  PL.cla()
  xr=[];yr=[];xb=[];yb=[];xk=[];yk=[]
  ag_counter = 0
  for ag in agents:
    xk.append(ag[3])
    yk.append(ag[4])
    if time >= 1:
      PL.plot([ag[0], ag[3]], [ag[1], ag[4]], 'g-', label="Route to destination")
      PL.plot(destination_trace_x_list[ag_counter], destination_trace_y_list[ag_counter], color='gray', linestyle=':')
    if ag[2] == 1:
      xr.append(ag[0])
      yr.append(ag[1])
      ag[2] = 0
    else:
      xb.append(ag[0])
      yb.append(ag[1])
    ag_counter += 1
  PL.plot([0.0], [0.0], 'ro', label="Home", markersize=9) # home position
  PL.plot(xk, yk, 'k.', label="Destination")
  PL.plot(xr, yr, 'ro')
  PL.plot(xb, yb, 'bo', label="Current location")
  PL.legend(loc='best') 
  PL.axis('scaled')
  PL.axis([width[0], width[1], height[0], height[1]])
  PL.title('Time: t = ' + str(time))

# walker's destination is kept inside the system
def clip(a, b, angle, amin, amax, bmin, bmax):
  if a < amin: 
    b += (amin-a)*math.tan(angle)
    a = amin
  elif a > amax: 
    b -= (a-amax)*math.tan(angle)
    a = amax

  if angle == math.pi/2.0:
    b = bmax
  elif angle == -math.pi/2.0:
    b = bmin
  else:
    if b < bmin: 
      a += (bmin-b)/math.tan(angle)
      b = bmin
    elif b > bmax: 
      a -= (b-bmax)/math.tan(angle)
      b = bmax
  return a, b

# PyCX step
def step():
  global time, agents

  # increment time
  time += 1
  #print("time:", time)

  ag_counter = 0
  for ag in agents:
    if ag[5] == 'stop':
      # determine the next destination
      ag[6] = RD.uniform(-math.pi, math.pi)
      dist_to_dest = NP.random.pareto(scaling_exponent)
      ag[3] = ag[0] + dist_to_dest * math.cos(ag[6])
      ag[4] = ag[1] + dist_to_dest * math.sin(ag[6])
      ag[3], ag[4] = clip(ag[3], ag[4], ag[6], width[0], width[1], height[0], height[1])
      destination_trace_x_list[ag_counter].append( ag[3] )
      destination_trace_y_list[ag_counter].append( ag[4] )
      ag[5] = 'move'
    elif ag[5] == 'move':
      if (ag[4]-ag[1])*(ag[4]-ag[1])+(ag[3]-ag[0])*(ag[3]-ag[0]) > move_speed*move_speed:
        # move a single step
        ag[0] += move_speed * math.cos(ag[6])
        ag[1] += move_speed * math.sin(ag[6])
      else:
        ag[0] = ag[3]
        ag[1] = ag[4]
        ag[9] = int(NP.random.pareto(wait_exponent)) # duration of stay
        ag[5] = 'stay'
    elif ag[5] == 'stay':
      if ag[9] <= 1:
        ag[9] = 0
        ag[5] = 'reach'
      else:
        ag[9] -= 1
    elif ag[5] == 'reach':
      if RD.uniform(0,1) < homesick_prob:
        ag[5] = 'home'
      else:
        ag[5] = 'stop'
    elif ag[5] == 'home':
      ag[6] = math.atan2(ag[8]-ag[1], ag[7]-ag[0])
      ag[3] = ag[7]
      ag[4] = ag[8]
      destination_trace_x_list[ag_counter].append( ag[3] )
      destination_trace_y_list[ag_counter].append( ag[4] )
      ag[5] = 'move'
    ag_counter += 1


# simulation starts here
import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
