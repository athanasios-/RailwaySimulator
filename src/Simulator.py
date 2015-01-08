'''
Created on Dec 23, 2014

@author: ubuntu
'''
from Station import Station
from Train import Train
from Cargo import Cargo

class Simulator(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        #create stations
        self.station_a = Station('A')
        self.station_b = Station('B')
        self.station_a.add_next_station(self.station_b)
        self.station_b.add_next_station(self.station_a)
        #create trains
        self.train_a = Train(1,1,'t_a')
        #create cargo
        self.cargo_a = Cargo(self.station_b)
        #allocate cargo
        self.station_a.add_cargo(self.cargo_a)
    
    def Start(self):
        self.station_a.init()
        self.station_b.init()
        self.station_a.dock_train(self.train_a)
    
    def stop(self):
        self.station_a.stop()
        self.station_b.stop()