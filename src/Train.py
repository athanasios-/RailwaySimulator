'''
Created on Dec 22, 2014

@author: ubuntu
'''
from time import sleep

class Train(object):
    '''
    classdocs
    '''

    def __init__(self, speed, capacity, name):
        '''
        Constructor
        '''
        self.speed = speed
        self.__capacity = capacity
        self.name = name
        self.__cargo = []
    
    def num_of_train_cargo(self):
        return len(self.__cargo)
    
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self,speed):
        self.__speed = speed
    
    @property
    def available_capacity(self):
        return  self.__capacity - self.num_of_train_cargo()
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name
    
    def travel(self):
        sleep(float(3/self.speed))
    
    def load_cargo(self, cargo):
        if self.available_capacity > 0:
            print ('loading cargo to %s' % cargo.destination.name)
            self.__cargo.append(cargo)
            cargo.load()
    
    def unload_cargo(self, station):
        for c in self.__cargo:
            if c.destination is station:
                print ('unloading cargo at %s' % station.name)
                self.__cargo.remove(c)
                c.unload()
            
        