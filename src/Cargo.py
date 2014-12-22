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
    
    def Destination(self):
        return self.destination
    
    def Load(self):
        sleep(3)
    
    def Unload(self):
        sleep(3)