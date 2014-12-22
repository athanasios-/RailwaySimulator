'''
Created on Dec 22, 2014

@author: ubuntu
'''
from time import sleep

class Train(object):
    '''
    classdocs
    '''

    def __init__(self, speed, capacity, id):
        '''
        Constructor
        '''
        self.speed = speed
        self.capacity = capacity
        self.id = id
        self.cargo = []
    
    def Cargo(self):
        return self.cargo
    
    def Speed(self):
        return self.speed
    
    def Capacity(self):
        return self.capacity
    
    def Id(self):
        return self.id
    
    def Travel(self, station):
        sleep(float(3/self.speed))
        station.AddTrain(self)
    
    def LoadCargo(self, cargo):
        self.cargo.append(cargo)
        cargo.Load()
    
    def UnloadCargo(self, station):
        for c in self.cargo:
            if c.Destination() is station:
                self.cargo.remove(c)
                c.Unload()
            
        