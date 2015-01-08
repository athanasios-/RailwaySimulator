'''
Created on Dec 22, 2014

@author: ubuntu
'''
import unittest
import time
from Cargo import Cargo
from Train import Train

class MockStation(object):
    def __init__(self):
        self.trains = []
    
    def add_train(self, train):
        self.trains.append(train)
    
    def name(self):
        pass
    
    def dock_train(self, train):
        self.add_train(train)

class TrainTest(unittest.TestCase):

    def setUp(self):
        self.train = Train(1, 2, 'tA')
        self.mockStation = MockStation()
        self.cargo = Cargo(self.mockStation)

    def testSpeed(self):
        self.assertEqual(1, self.train.speed, 'train has speed')
    
    def testCapacity(self):
        self.assertEqual(2, self.train.available_capacity, 'train has capacity')
    
    def testId(self):
        self.assertEqual('tA', self.train.name, 'train has id')
        
    def testTravelTime(self):
        startTime = time.time()
        self.train.travel(self.mockStation)
        self.assertGreaterEqual(time.time() - startTime, float(3/self.train.speed))
        
    def testTravelArrivalToStation(self):
        self.train.travel(self.mockStation)
        self.assertEqual(1, len(self.mockStation.trains), '1 train arrived to station')
        
    def testLoadCargoLoadingTime(self):
        startTime = time.time()
        self.train.load_cargo(self.cargo)
        self.assertGreaterEqual(time.time() - startTime, 3)
    
    def testLoadCargoAdditionToTrainCargo(self):
        self.train.load_cargo(self.cargo)
        self.assertEqual(1, self.train.num_of_train_cargo())
        
    def testUnloadCargoUnloadingTime(self):
        self.train.load_cargo(self.cargo)
        startTime = time.time()
        self.train.unload_cargo(self.mockStation)
        self.assertGreaterEqual(time.time() - startTime, 3)
        
    def testUnlodCargoRemoveFromTrainCargo(self):
        self.train.load_cargo(self.cargo)
        self.train.unload_cargo(self.mockStation)
        self.assertEqual(0, self.train.num_of_train_cargo())
    
    def testUnlodCargoMultipleCargoDestinations(self):
        new_station = MockStation()
        new_cargo = Cargo(new_station)
        self.train.load_cargo(self.cargo)
        self.train.load_cargo(new_cargo)
        self.train.unload_cargo(self.mockStation)
        self.assertEqual(1, self.train.num_of_train_cargo())
        
if __name__ == "__main__":
    unittest.main()