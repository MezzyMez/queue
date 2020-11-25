#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 08:56:13 2020

@author: Mez
"""


from node import Node

class Queue:
  # Add max_size and size properties within __init__():
  def __init__(self, max_size=None, size=0):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = size
    
  def peek(self):
    if self.is_empty():
      print ("Nothing to see here!")
    else:
      return self.head.get_value()
  
  # Define get_size() and has_space() below:
  def get_size(self):
    return self.size
  
  def has_space(self):
    if self.max_size:
      return True if (self.max_size>self.get_size()) else False
    else:
      return True
    
  def is_empty(self):
    return self.size == 0