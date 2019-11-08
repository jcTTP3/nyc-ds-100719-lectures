#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:12:26 2019

@author: marshall132
"""

class Calculator:
    def __init__(self, data):
        self.data = data
        self.length = len(data)
        self.mean = self.average()
        self.median = self.middle()
        self.variance = self._variance()
        self.stand_dev = self.sqt()
    
    def average(self):
        return sum(self.data)/self.length
    
    def middle(self):
        data_sorted = sorted(self.data)
        if len(data_sorted) % 2:
            return data_sorted[(len(data_sorted)//2)]
        else:
            return (data_sorted[(len(data_sorted)//2)-1] + data_sorted[(len(data_sorted)//2)])/2
        
    def _variance(self):
        diffs = []
        for item in self.data:
            diffs.append((item-self.mean)**2)
        return sum(diffs)/(len(diffs)-1)
    
    def sqt(self):
        return self.variance ** 0.5
    
    def add_data(self, new_data):
        return self.data.extend(new_data)
    
    def remove_data(self, data_to_remove):
        for item in data_to_remove:
            if item in self.data:
                self.data.remove(item)
    
        
#x = Calculator([5,10,15,20])
#y = [3,10,14]