# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:34:27 2023

@author: 208-PC
"""

class TV :
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
        
    def show(self):
        print(self.channel, self.volume, self.on)
        
    def setChannel(self, channel):
        self.channel = channel
        
    def getChannel(self):
        return self.channel
    
t = TV(9, 10, True)
t.show()

t.setChannel(120)
t.show()