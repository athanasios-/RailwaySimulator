'''
Created on Dec 23, 2014

@author: ubuntu
'''
import threading
from TrackSegment import TrackSegment

class Station(object):
    '''
    classdocs
    '''

    def __init__(self, name):
        '''
        Constructor
        '''
        self.__stockedCargo = []
        self.__dockedTrains = []
        self.name = name
        self.__active = True
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name
    
    def num_of_station_cargo(self):
        return len(self.__stockedCargo)
    
    def add_cargo(self, cargo):
        self.__stockedCargo.append(cargo)
    
    def dock_train(self, train):
        self.__dockedTrains.append(train)
        print('Train ' + train.name + ' at ' + self.name)
    
    def num_of_docked_trains(self):
        return len(self.__dockedTrains)
    
    def add_next_station(self, nextStation):
        self.trackSegment = TrackSegment(self.name + '-' + nextStation.name, nextStation)
    
    def serve_next(self):
        while self.__dockedTrains:
            topTrain = self.__dockedTrains.pop()
            self._unload_train(topTrain)
            self._load_train(topTrain)
            self._route_train(topTrain)
    
    def _unload_train(self, train):
        train.unload_cargo(self)
    
    def _load_train(self, train):
        while len(self.__stockedCargo) > 0 and train.available_capacity > 0:
            train.load_cargo(self.__stockedCargo.pop())
    
    def _route_train(self, train):
        self.trackSegment.add_train(train)
            
    def init(self):
        self.trackSegment.init()
        self.t1 = threading.Thread(target=self._loop_serve_next)
        self.t1.start()
    
    def _loop_serve_next(self):
        while self.__active:
            self.serve_next()
            
    def stop(self):
        self.trackSegment.stop()
        self.__active = False
        self.t1.join()
        print(self.name + ' inactive')
    
    