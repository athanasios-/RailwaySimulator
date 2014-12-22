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
    
    def AddTrain(self, train):
        self.trains.append(train)

class Test(unittest.TestCase):

    def setUp(self):
        self.train = Train(1, 2, 'tA')
        self.mockStation = MockStation()
        self.cargo = Cargo(self.mockStation)

    def testSpeed(self):
        self.assertEqual(1, self.train.Speed(), 'train has speed')
    
    def testCapacity(self):
        self.assertEqual(2, self.train.Capacity(), 'train has capacity')
    
    def testId(self):
        self.assertEqual('tA', self.train.Id(), 'train has id')
        
    def testTravelTime(self):
        startTime = time.time()
        self.train.Travel(self.mockStation)
        self.assertGreaterEqual(time.time() - startTime, float(3/self.train.Speed()))
        
    def testTravelArrivalToStation(self):
        self.train.Travel(self.mockStation)
        self.assertEqual(1, len(self.mockStation.trains), '1 train arrived to station')
        
    def testLoadCargoLoadingTime(self):
        startTime = time.time()
        self.train.LoadCargo(self.cargo)
        self.assertGreaterEqual(time.time() - startTime, 3)
    
    def testLoadCargoAdditionToTrainCargo(self):
        self.train.LoadCargo(self.cargo)
        self.assertEqual(1, len(self.train.Cargo()))
        
    def testUnloadCargoUnloadingTime(self):
        self.train.LoadCargo(self.cargo)
        startTime = time.time()
        self.train.UnloadCargo(self.mockStation)
        self.assertGreaterEqual(time.time() - startTime, 3)
        
    def testUnlodCargoRemoveFromTrainCargo(self):
        self.train.LoadCargo(self.cargo)
        self.train.UnloadCargo(self.mockStation)
        self.assertEqual(0, len(self.train.Cargo()))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()