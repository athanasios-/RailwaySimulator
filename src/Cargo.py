'''
Created on Dec 22, 2014

@author: ubuntu
'''
from time import sleep

class Cargo(object):
    '''
    classdocs
    '''

    def __init__(self, destination):
        '''
        Constructor
        '''
        self.destination = destination;
        
    @property
    def destination(self):
        return self.__destination
    
    @destination.setter
    def destination(self,destination):
        self.__destination = destination
    
    def load(self):
        sleep(3)
    
    def unload(self):
        sleep(3)