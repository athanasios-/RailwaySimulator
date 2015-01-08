'''
Created on Dec 23, 2014

@author: ubuntu
'''
import unittest
from Cargo import Cargo
from Train import Train
from Station import Station

class StationTest(unittest.TestCase):

    def setUp(self):
        self.train = Train(1, 1, 'testTrain')
        self.station = Station('A')
        self.next_station = Station('B')
        self.station.add_next_station(self.next_station)

    def testCargoEmpty(self):
        self.assertEqual(0, self.station.num_of_station_cargo())
        
    def testAddCargo(self):
        self.station.add_cargo('cargo')
        self.assertEqual(1, self.station.num_of_station_cargo())
    
    def testDockedTrainsEmpty(self):
        self.assertEqual(0, self.station.num_of_docked_trains())
        
    def testDockTrain(self):
        self.station.dock_train(Train(1,1,"cargo train"))
        self.assertEqual(1, self.station.num_of_docked_trains())
    
    def testServeNextSigleTrainWithOneCargo(self):
        cargo = Cargo(self.station)
        train_with_cargo = Train(1,1,"cargo train")
        train_with_cargo.load_cargo(cargo)
        self.station.dock_train(train_with_cargo)
        self.station.serve_next()
        self.assertEqual(0, train_with_cargo.num_of_train_cargo())
    
    def testServeNextSigleTrainWithOneCargoOneStationStockedCargo(self):
        station_cargo = Cargo(self.next_station)
        self.station.add_cargo(station_cargo)
        train_cargo = Cargo(self.station)
        train_with_cargo = Train(1,1,"train_cargo")
        train_with_cargo.load_cargo(train_cargo)
        self.station.dock_train(train_with_cargo)
        self.station.serve_next()
        self.assertEqual(1, train_with_cargo.num_of_train_cargo())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()