'''
Created on Dec 23, 2014

@author: ubuntu
'''
import threading
class TrackSegment(object):
    '''
    classdocs
    '''

    def __init__(self, name, destinationStation):
        '''
        Constructor
        '''
        self.name = name
        self.__destinationStation = destinationStation
        self.__trains = []
        self.__active = True;
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name
    
    def add_train(self, train):
        self.__trains.append(train)
    
    def num_of_trains(self):
        return len(self.__trains)
    
    def init(self):
        self.t1 = threading.Thread(target=self._loop_route)
        self.t1.start()
    
    def _loop_route(self):
        while self.active:
            self._route()
    
    def stop(self):
        self.__active = False
        self.t1.join()
        print(self.name + ' inactive')
    
    def _route(self):
        while self.__trains:
            top_train = self.__trains.pop()
            top_train.travel()
            self.__destinationStation.dock_train(top_train)